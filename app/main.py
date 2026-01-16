from fastapi import FastAPI

from app.database import engine, Base
from app.routes.auth import router as auth_router


from app.models.user import User
from app.models.agent import Agent
from app.models.vehicle import Vehicle
from app.models.wash_package import WashPackage
from app.models.booking import Booking
from app.models.subscription import Subscription
from app.routes.auth import router as auth_router
from app.routes.users import router as users_router
from app.routes.vehicle import router as vehicle_router
from app.routes.booking import router as booking_router




app = FastAPI(
    title="WIPERS API",
    description="On-demand vehicle wash booking platform",
    version="1.0.0"
)

app.include_router(auth_router)
app.include_router(users_router)
app.include_router(vehicle_router)
app.include_router(booking_router)




@app.on_event("startup")
def startup():
    Base.metadata.create_all(bind=engine)

