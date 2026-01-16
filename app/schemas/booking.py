from pydantic import BaseModel
from uuid import UUID
from datetime import datetime


class BookingCreate(BaseModel):
    vehicle_id: UUID
    package_id: UUID
    scheduled_time: datetime


class BookingOut(BaseModel):
    id: UUID
    vehicle_id: UUID
    package_id: UUID
    status: str
    scheduled_time: datetime

    class Config:
        from_attributes = True
