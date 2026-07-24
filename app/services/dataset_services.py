from sqlalchemy.orm import Session 
from app.models.dataset import Dataset

class DatasetService:
    @staticmethod
    def create_dataset(db:Session,project_id,uploaded_file_id,analysis)-> Dataset:
        dataset=Dataset(
            project_id = project_id,
            uploaded_file_id = uploaded_file_id,
            row=analysis["row"],
            columns=analysis["columns"],
            missing_values=analysis["missing_values"],
            duplicate_rows=analysis["duplicate_rows"]
        )

        db.add(dataset)
        db.commit()
        db.refresh(dataset)
        
        return dataset