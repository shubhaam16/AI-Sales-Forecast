from fastapi import APIRouter ,Depends
from sqlalchemy.orm import Session

from app.database.database import get_db
from app.schemas.project import ProjectResponse
from app.services.project_services import ProjectService

router = APIRouter (
    prefix= "/project",
    tags=["Projects"]
)

@router.get("/", response_model=list[ProjectResponse])
def get_projects(db: Session = Depends(get_db)):
    return ProjectService.get_all_projects(db)