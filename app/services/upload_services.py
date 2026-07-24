from pathlib import Path
from uuid import UUID

from fastapi import HTTPException, UploadFile
from sqlalchemy.orm import Session

from app.models.uploaded_file import UploadedFile
from app.schemas.upload import UploadResponse, DatasetSummaryResponse
from app.storage.local_storage import LocalStorage
from app.utils.file_validator import FileValidator
from app.utils.dataset_reader import DatasetReader
from app.utils.dataset_analyzer import DatasetAnalyzer
from app.services.dataset_services import DatasetService
from app.utils.dataset_cleaner import DatasetCleaner

class UploadServices:

    @staticmethod
    async def upload_file(
        db: Session,
        project_id: UUID,
        file: UploadFile
    ) -> UploadResponse:

        await FileValidator.validate(file)

        file_path = LocalStorage.save_file(str(project_id), file)

        df = DatasetReader.read(file_path)
        analysis = DatasetAnalyzer.analyze(df)
        cleaned_df , cleaning_report = DatasetCleaner.clean(df)

        try:
            stored_filename = Path(file_path).name
            file_size = Path(file_path).stat().st_size
            file_extension = Path(file.filename).suffix.lower()

            uploaded_file = UploadedFile(
                project_id=project_id,
                original_filename=file.filename,
                stored_filename=stored_filename,
                file_path=file_path,
                file_size=file_size,
                file_type=file_extension,
                status="UPLOADED"
            )

            db.add(uploaded_file)
            db.commit()
            db.refresh(uploaded_file)

            dataset = DatasetService.create_dataset(db=db,project_id=project_id,uploaded_file_id=uploaded_file.id,analysis=analysis)

            return UploadResponse(
                    upload_id=uploaded_file.id,
                    dataset_id=dataset.id,
                    message="File uploaded successfully",
                    project_id=project_id,
                    original_filename=file.filename,
                    stored_filename=stored_filename,
                    stored_path=file_path,
                    uploaded_at=uploaded_file.uploaded_at,

                    dataset_summary=DatasetSummaryResponse(
                        rows=analysis["rows"],
                        columns=analysis["columns"],
                        column_names=analysis["column_names"],
                        sheet_names=None
                    ),

                    cleaning_report=CleaningReportResponse(
                        original_rows=cleaning_report["original_rows"],
                        original_columns=cleaning_report["original_columns"],
                        missing_values_before=cleaning_report["missing_values_before"],
                        missing_values_after=cleaning_report["missing_values_after"],
                        duplicate_rows_before=cleaning_report["duplicate_rows_before"],
                        duplicate_rows_after=cleaning_report["duplicate_rows_after"],
                        final_rows=cleaning_report["final_rows"]
                    )
                )

        except Exception as e:
            db.rollback()
            LocalStorage.delete_file(file_path)

            raise HTTPException(
                status_code=500,
                detail=f"Upload failed: {str(e)}"
            )