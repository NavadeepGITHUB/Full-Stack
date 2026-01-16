import uuid
from sqlalchemy import Column, String, Integer, Boolean, DateTime
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func

from app.database import Base


class WashPackage(Base):
    __tablename__ = "wash_packages"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)

    name = Column(String(100), nullable=False)  # Quick Wash, Deep Clean
    description = Column(String(255), nullable=True)

    price = Column(Integer, nullable=False)      # price in INR
    duration_minutes = Column(Integer, nullable=False)

    is_active = Column(Boolean, default=True)

    created_at = Column(DateTime(timezone=True), server_default=func.now())
