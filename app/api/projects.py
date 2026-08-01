from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from uuid import UUID

from app.database.database import get_db
from app.schemas.project import ProjectResponse, ProjectCreate, ProjectUpdate
from app.services.project_services import ProjectService

router = APIRouter(
    prefix="/project",
    tags=["Projects"]
)

@router.get("/", response_model=list[ProjectResponse])
def get_all_projects(db: Session = Depends(get_db)):
    try:
        return ProjectService.get_all_projects(db)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error fetching projects: {str(e)}")

@router.get("/{project_id}", response_model=ProjectResponse)
def get_project(project_id: UUID, db: Session = Depends(get_db)):
    project = ProjectService.get_project(db, project_id)
    if not project:
        raise HTTPException(status_code=404, detail="Project not found")
    return project

@router.post("/", response_model=ProjectResponse)
def create_project(project_data: ProjectCreate, db: Session = Depends(get_db)):
    return ProjectService.create_project(db, project_data)

@router.delete("/{project_id}")
def delete_project(project_id: UUID, db: Session = Depends(get_db)):
    try:
        deleted = ProjectService.delete_project(db, project_id)
        if not deleted:
            raise HTTPException(status_code=404, detail="Project not found")
        return {"message": "Project deleted successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error deleting project: {str(e)}")
