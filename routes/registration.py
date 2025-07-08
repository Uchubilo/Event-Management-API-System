from fastapi import APIRouter, HTTPException
from schemas.registration import RegistrationCreate, RegistrationBase, Registration
from services.registration import registration_service

registration_router = APIRouter()

@registration_router.post("/", status_code=201)
def create_registration(registration_data: RegistrationBase):
  registration = registration_service.create_registration(registration_data)
  return {"message": "Registration created successfully", "registration_details": registration}

@registration_router.get("/", status_code=200)
def get_registrations():
  return registration_service.get_registrations()

@registration_router.get("/{registration_id}", status_code=200)
def get_registration_by_id(registration_id: str):
  registration = registration_service.get_registration_by_id(registration_id)
  if not registration:
    raise HTTPException(status_code=404, detail="Registration not found.")
  return registration

@registration_router.post("/{registration_id}/attendance", status_code=200)
def mark_attendance(registration_id: str):
  registration = registration_service.mark_attendance(registration_id)
  if not registration:
    raise HTTPException(status_code=404, detail="Registration not found")
  return {"message": "Attendance marked successfully", "registration": registration}


@registration_router.get("/{user_id}/events", status_code=200)
def track_user_attendance(user_id: int):
  registrations = registration_service.get_registrations()
  user_events = [reg for reg in registrations if reg.user_id == user_id and reg.attended == True]
  if not user_events:
    raise HTTPException(status_code=404, detail="No event(s) found for this user")
  return {"user_id": user_id, "events": user_events}