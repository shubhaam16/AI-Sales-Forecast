from sqlalchemy import Column, DateTime, ForeignKey, Integer, text
from sqlalchemy.dialects.postgresql import UUID

from app.database.database import Base


class Dataset(Base):
    __tablename__ = "datasets"
    __table_args__ = {"schema": "sales_app"}

    id = Column(
        UUID(as_uuid=True),
        primary_key=True,
        server_default=text("gen_random_uuid()")
    )

    project_id = Column(
        UUID(as_uuid=True),
        ForeignKey("sales_app.projects.id"),
        nullable=False
    )

    uploaded_file_id = Column(
        UUID(as_uuid=True),
        ForeignKey("sales_app.uploaded_files.id"),
        nullable=False
    )

    rows = Column(
        Integer,
        nullable=False
    )

    columns = Column(
        Integer,
        nullable=False
    )

    missing_values = Column(
        Integer,
        nullable=False
    )

    duplicate_rows = Column(
        Integer,
        nullable=False
    )

    created_at = Column(
        DateTime,
        server_default=text("CURRENT_TIMESTAMP")
    )