from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from datetime import datetime

from app.database import get_db
from app.dependencies import get_current_user
from app.models.user import User
from app.models.booking import Booking
from app.models.vehicle import Vehicle
from app.models.wash_package import WashPackage
from app.models.agent import Agent
from app.schemas.booking import BookingCreate, BookingOut

router = APIRouter(
    prefix="/bookings",
    tags=["Bookings"]
)


@router.post("/", response_model=BookingOut, status_code=201)
def create_booking(
    booking: BookingCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    # 1. Check vehicle belongs to user
    vehicle = db.query(Vehicle).filter(
        Vehicle.id == booking.vehicle_id,
        Vehicle.user_id == current_user.id
    ).first()

    if not vehicle:
        raise HTTPException(status_code=404, detail="Vehicle not found")

    # 2. Check package exists
    package = db.query(WashPackage).filter(
        WashPackage.id == booking.package_id,
        WashPackage.is_active == True
    ).first()

    if not package:
        raise HTTPException(status_code=404, detail="Wash package not found")

    # 3. Find available agent
    agent = db.query(Agent).filter(
        Agent.is_available == True,
        Agent.is_active == True
    ).first()

    # 4. Decide booking status
    if agent:
        status_value = "CONFIRMED"
        agent_id = agent.id
        agent.is_available = False  
    else:
        status_value = "PENDING"
        agent_id = None

    # 5. Create booking
    new_booking = Booking(
        user_id=current_user.id,
        vehicle_id=booking.vehicle_id,
        package_id=booking.package_id,
        agent_id=agent_id,
        status=status_value,
        scheduled_time=booking.scheduled_time,
        created_at=datetime.utcnow()
    )

    db.add(new_booking)
    db.commit()
    db.refresh(new_booking)

    return new_booking
