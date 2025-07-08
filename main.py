
from fastapi import FastAPI

# Importing individual route modules for different resources
from routes.user import user_router
from routes.event import event_router
from routes.registration import registration_router

# Initialize the FastAPI application
app = FastAPI(
    title="Event Management API",
    description="API for managing users, events, and registrations in an event management system.",
    version="1.0.0"
)

# Include user-related routes with the '/users' URL prefix
app.include_router(
    user_router, 
    prefix="/users", 
    tags=["Users"]  # Used for grouping endpoints in the documentation
)

# Include event-related routes with the '/events' URL prefix
app.include_router(
    event_router, 
    prefix="/events", 
    tags=["Events"]
)

# Include registration-related routes with the '/registrations' URL prefix
app.include_router(
    registration_router, 
    prefix="/registrations", 
    tags=["Registrations"]
)
