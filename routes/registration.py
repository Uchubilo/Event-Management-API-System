from fastapi import APIRouter, HTTPException
from schemas.registration import RegistrationBase
from services.registration import registration_service

registration_router = APIRouter(prefix="/registrations", tags=["Registrations"])

@registration_router.post("/", status_code=201)
def create_registration(registration_data: RegistrationBase):
    result = registration_service.create_registration(registration_data)
    return {
        "message": "Registration created successfully",
        "registration": result.get("registration")
    }

@registration_router.get("/", status_code=200)
def get_registrations():
    result = registration_service.get_registrations()
    return {
        "message": "All registrations retrieved",
        "registrations": result.get("registrations")
    }

@registration_router.get("/{registration_id}", status_code=200)
def get_registration_by_id(registration_id: str):
    try:
        result = registration_service.get_registration_by_id(registration_id)
        return result
    except HTTPException:
        raise HTTPException(status_code=404, detail="Registration not found")


@registration_router.post("/{registration_id}/attendance", status_code=200)
def mark_attendance(registration_id: str):
    try:
        result = registration_service.mark_attendance(registration_id)
        return {
            "message": "Attendance marked successfully",
            "registration": result.get("registration")
        }
    except HTTPException:
        raise HTTPException(status_code=404, detail="Registration not found")


@registration_router.get("/user/{user_id}/events", status_code=200)
def track_user_attendance(user_id: int):
    result = registration_service.get_registrations()
    all_registrations = result.get("registrations", [])
    user_events = [reg for reg in all_registrations if reg.user_id == user_id and reg.attended]

    if not user_events:
        raise HTTPException(status_code=404, detail="No attended events found for this user")

    return {
        "user_id": user_id,
        "attended_events": user_events
    }
