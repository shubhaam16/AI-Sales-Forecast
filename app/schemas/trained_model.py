from uuid import UUID

from pydantic import BaseModel

from datetime import datetime


class TrainedModelCreate(BaseModel):

    project_id: UUID

    dataset_id: UUID

    model_name: str

    algorithm: str

    model_path: str

    mae: float

    rmse: float

    r2_score: float


class TrainedModelResponse(BaseModel):

    id: UUID

    project_id: UUID

    dataset_id: UUID

    model_name: str

    algorithm: str

    model_path: str

    mae: float

    rmse: float

    r2_score: float

    is_active: bool

    created_at: datetime

    class Config:
        from_attributes = True