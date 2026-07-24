from sqlalchemy import (Column,
    DateTime,
    ForeignKey,
    Integer,
    String,
    text
)
from sqlalchemy.dialects.postgresql import UUID

from app.database.database import Base


class UploadedFile(Base):
    __tablename__ = "uploaded_files"
    __table_args__ = {"schema": "sales_app"}

    id = Column(
        UUID(as_uuid=True),
        primary_key=True,
        server_default=text ("gen_random_uuid()")
    )

    project_id = Column(
        UUID(as_uuid=True),
        ForeignKey("sales_app.projects.id"),
        nullable=False
    )

    original_filename = Column(
        String(255),
        nullable=False
    )

    stored_filename = Column(
        String(255),
        nullable=False
    )

    file_path = Column(
        String(500),
        nullable=False
    )

    file_size = Column(
        Integer,
        nullable=False
    )

    file_type = Column(
        String(20),
        nullable=False
    )

    uploaded_at = Column(
        DateTime,
        server_default=text("CURRENT_TIMESTAMP")
    )

    status = Column(
        String(30)
    )