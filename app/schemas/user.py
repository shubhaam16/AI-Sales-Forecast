from pydantic import BaseModel,EmailStr
from uuid import UUID
from datetime import datetime


class UserCreate(BaseModel):

    full_name: str
    email: EmailStr
    password: str

class UserUpdate(BaseModel):
    full_name:str
    email:EmailStr

class UserResponse (BaseModel):
    id :UUID
    full_name:str
    email:EmailStr
    role:str
    is_verified:bool
    is_active:bool
    created_at:datetime
    
class Config:
    from_attributes= True
    