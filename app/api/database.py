from fastapi import APIRouter
from sqlalchemy import text
from sqlalchemy.orm import Session
from fastapi import Depends 

from app.database.database import get_db


router = APIRouter (
    prefix="/database",
    tags=["Database"]
)


@router.get("/test")
def test_database(db: Session = Depends(get_db)):
    try:
        db.execute (text("SELECT 1"))
        return {
            "message ": "Database Connected Successfully "
        }
    except Exception as e :
        return{
            "message": "Error to connect the database ",
            "error": str(e)
        }