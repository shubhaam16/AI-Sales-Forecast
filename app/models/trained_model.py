import uuid

from sqlalchemy import (Column,String,Boolean,Float,DateTime,ForeignKey)

from sqlalchemy.dialects.postgresql import UUID

from sqlalchemy.sql import func

from app.database.database import Base


class TrainedModel(Base):

    __tablename__ = "trained_models"
    __table_args__ = {"schema": "sales_app"}

    id = Column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4
    )

    project_id = Column(
        UUID(as_uuid=True),
        ForeignKey("sales_app.projects.id"),
        nullable=False
    )

    dataset_id = Column(
        UUID(as_uuid=True),
        ForeignKey("sales_app.datasets.id"),
        nullable=False
    )

    model_name = Column(
        String,
        nullable=False
    )

    algorithm = Column(
        String,
        nullable=False
    )

    model_path = Column(
        String,
        nullable=False
    )

    mae = Column(Float)

    rmse = Column(Float)

    r2_score = Column(Float)

    is_active = Column(
        Boolean,
        default=False
    )

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )
