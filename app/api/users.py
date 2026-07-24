from fastapi import APIRouter
from fastapi import Depends
from sqlalchemy.orm import Session

from app.database.database import get_db
from app.schemas.user import UserResponse
from app.services.user_service import UserService

router = APIRouter(
    prefix="/users",
    tags=["Users"]
)

@router.get("/", response_model= list[UserResponse])
def get_users(db:Session = Depends(get_db)):
    return UserService.get_all_users(db)

@router.get("/{id}")
def get_user(db:Session = Depends (get_db)):
    return UserService.get_user(db)

@router.post("/")
def create_user(db:Session = Depends (get_db)):
    return UserService.create_user(db)

@router.delete("/{id}")
def delete_user(db:Session = Depends (get_db)):
    return UserService.delete_user(db)