from sqlalchemy import Boolean
from sqlalchemy import Column
from sqlalchemy import DateTime
from sqlalchemy import String
from sqlalchemy.dialects.postgresql import UUID

from app.database.database import Base 

class User(Base):

    __tablename__ = "users"
    __table_args__ = {"schema": "sales_app"}

    id = Column(UUID(as_uuid=True), primary_key=True)

    full_name = Column(String(150), nullable=False)

    email = Column(String(255), unique=True, nullable=False)

    password_hash = Column(String, nullable=False)

    role = Column(String(20), default="USER")

    is_verified = Column(Boolean, default=False)

    is_active = Column(Boolean, default=True)

    last_login = Column(DateTime)

    created_at = Column(DateTime)

    updated_at = Column(DateTime)