from fastapi import APIRouter
from fastapi import Depends
from sqlalchemy.orm import Session
from uuid import UUID                      # extra line add by me 
from app.models.user import User            # extra line add by me 

from app.database.database import get_db
from app.schemas.user import UserResponse,UserCreate
from app.services.user_service import UserService

router = APIRouter(
    prefix="/users",
    tags=["Users"]
)

@router.get("/", response_model= list[UserResponse])
def get_users(db:Session = Depends(get_db)):
    return UserService.get_all_users(db)

@router.get("/{id}")
def get_user(id:UUID,  db:Session = Depends (get_db)):
    return UserService.get_user(db,id)

@router.post("/", response_model=UserResponse)
def create_user(user_data: UserCreate  , db:Session = Depends (get_db)):
    return UserService.create_user(db ,user_data)

@router.delete("/{id}")
def delete_user(id:UUID,db:Session = Depends (get_db)):
    return UserService.delete_user(db,id)