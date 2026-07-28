from uuid import UUID 
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database.database import get_db
from app.schemas.trained_model import TrainedModelCreate, TrainedModelResponse
from app.services.model_service import ModelService
from typing import List

router = APIRouter(
    prefix="/model",
    tags=["Models"]
)

@router.post("/models", response_model=TrainedModelResponse, status_code=201)
def create_model(model_data: TrainedModelCreate, db: Session = Depends(get_db)):
    return ModelService.create_model(db, model_data)

@router.get("/models/{model_id}", response_model=TrainedModelResponse)
def get_model(model_id: UUID, db: Session = Depends(get_db)):
    model = ModelService.get_model(db, model_id)
    if model is None:
        raise HTTPException(status_code=404, detail="Model not found")
    return model

@router.get("/projects/{project_id}/models", response_model=List[TrainedModelResponse])
def list_models(project_id: UUID, db: Session = Depends(get_db)):
    return ModelService.list_models(db, project_id)

@router.patch("/models/{model_id}/activate", response_model=TrainedModelResponse)
def activate_model(model_id: UUID, db: Session = Depends(get_db)):
    model = ModelService.active_model(db, model_id)   # fixed name
    if model is None:
        raise HTTPException(status_code=404, detail="Model not found.")
    return model

@router.delete("/models/{model_id}")
def delete_model(model_id: UUID, db: Session = Depends(get_db)):
    deleted = ModelService.delete_model(db, model_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Model not found.")
    return {"message": "Model deleted successfully."}
