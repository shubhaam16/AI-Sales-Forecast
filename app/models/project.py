from sqlalchemy import Column, DateTime, ForeignKey, Integer, String, Text
from sqlalchemy.dialects.postgresql import UUID

from app.database.database import Base


class Project(Base):
    __tablename__ = "projects"
    __table_args__ = {"schema": "sales_app"}

    id = Column(UUID(as_uuid=True), primary_key=True)

    user_id = Column(UUID(as_uuid=True),ForeignKey("sales_app.users.id"),nullable=False)

    project_name = Column(String(255), nullable=False)

    description = Column(Text)

    business_type = Column(String(100))

    forecast_period = Column(Integer)

    status = Column(String(50))

    created_at = Column(DateTime)

    updated_at = Column(DateTime)