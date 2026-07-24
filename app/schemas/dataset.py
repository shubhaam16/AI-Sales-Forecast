from datetime import datetime
from uuid import UUID

from pydantic import BaseModel


class DatasetCreate(BaseModel):
    project_id: UUID
    uploaded_file_id: UUID
    rows: int
    columns: int
    missing_values: int
    duplicate_rows: int


class DatasetResponse(BaseModel):
    id: UUID
    project_id: UUID
    uploaded_file_id: UUID
    rows: int
    columns: int
    missing_values: int
    duplicate_rows: int
    created_at: datetime

    model_config = {
        "from_attributes": True
    }