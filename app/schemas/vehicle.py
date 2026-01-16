from pydantic import BaseModel
from uuid import UUID
from typing import Optional


class VehicleCreate(BaseModel):
    vehicle_type: str
    vehicle_number: str
    brand: Optional[str] = None
    model: Optional[str] = None


class VehicleOut(BaseModel):
    id: UUID
    vehicle_type: str
    vehicle_number: str
    brand: Optional[str]
    model: Optional[str]

    class Config:
        from_attributes = True
