from datetime import datetime
from uuid import UUID

from pydantic import BaseModel


class ProjectCreate(BaseModel):
    user_id: UUID
    project_name: str
    description: str | None = None
    business_type: str
    forecast_period: int


class ProjectUpdate(BaseModel):
    project_name: str
    description: str | None = None
    business_type: str
    forecast_period: int


class ProjectResponse(BaseModel):
    id: UUID
    user_id: UUID
    project_name: str
    description: str | None = None
    business_type: str
    forecast_period: int
    status: str
    created_at: datetime

    class Config:
        from_attributes = True