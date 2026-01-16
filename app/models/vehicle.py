import uuid
from sqlalchemy import Column, String, DateTime, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func

from app.database import Base


class Vehicle(Base):
    __tablename__ = "vehicles"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)

    user_id = Column(UUID(as_uuid=True), nullable=False)
    vehicle_type = Column(String(50), nullable=False)   # Car, Bike, SUV
    vehicle_number = Column(String(20), unique=True, nullable=False)
    brand = Column(String(50), nullable=True)
    model = Column(String(50), nullable=True)

    created_at = Column(DateTime(timezone=True), server_default=func.now())
