from datetime import datetime
from uuid import UUID
from pydantic import BaseModel
from app.schemas.cleaning import CleaningReportResponse

class DatasetSummaryResponse(BaseModel):
    rows: int
    columns: int
    column_names: list[str]
    sheet_names: list[str] | None = None

class UploadResponse(BaseModel):
    upload_id: UUID
    dataser_id: UUID
    message: str
    project_id: UUID
    original_filename: str
    stored_filename: str
    stored_path: str
    uploaded_at: datetime
    dataset_summary: DatasetSummaryResponse
    cleaning_report: CleaningReportResponse
    

class FileSummaryResponse(BaseModel):
    filename: str
    rows: int
    columns: int
    column_names: list[str]
    sheet_names: list[str] | None = None



