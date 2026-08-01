from uuid import UUID 
from pydantic import BaseModel

class TrainModelRequest(BaseModel):
    project_id: UUID
    dataset_id: UUID
    target_column: str
    algorithm: str = "random_forest"
    test_size: float = 0.2

class TrainModelResponse(BaseModel):
    model_id: UUID
    algorithm: str
    mae: float
    rmse: float
    r2_score: float
    message: str