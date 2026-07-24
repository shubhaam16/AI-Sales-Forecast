from uuid import UUID 

from fastapi import APIRouter,Depends,File,Form ,UploadFile
from sqlalchemy.orm import Session

from app.database.database import get_db
from app.schemas.upload import UploadResponse
from app.services.upload_services import UploadServices

router = APIRouter (
    prefix="/upload",
    tags=["Uploads"]
)

@router.post("/",response_model=UploadResponse,status_code=201)
async def upload_file(
    project_id: UUID = Form(...),
    file: UploadFile = File(...),
    db: Session = Depends(get_db)
):
    """
    Upload an Excel or CSV file for a project.
    """

    return await UploadServices.upload_file(
        db=db,
        project_id=project_id,
        file=file
    )