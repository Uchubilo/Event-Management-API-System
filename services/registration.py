from fastapi import HTTPException
from schemas.registration import RegistrationBase
from database import registrations
from model import Registration as RegistrationModel
from services.user import user_service
from services.event import event_service
import uuid


class RegistrationService:

    @staticmethod
    def create_registration(registration_data: RegistrationBase):
        user = user_service.get_user_by_id(registration_data.user_id)
        if not user:
            raise HTTPException(status_code=404, detail="User ID does not exist")

        if not user.is_active:
            raise HTTPException(status_code=400, detail="User is not active")

        event_response = event_service.get_event(registration_data.event_id)
        event = event_response.get("event") if isinstance(event_response, dict) else None

        if not event:
            raise HTTPException(status_code=404, detail="Event ID does not exist")

        if not event.is_open:
            raise HTTPException(status_code=400, detail="Event is closed for registration")

        if any(
            reg.user_id == registration_data.user_id and reg.event_id == registration_data.event_id
            for reg in registrations
        ):
            raise HTTPException(status_code=400, detail="User already registered for this event")

        new_registration = RegistrationModel(
            id=str(uuid.uuid4()),
            user_id=registration_data.user_id,
            event_id=registration_data.event_id,
            registration_date=registration_data.registration_date,
            attended=False
        )

        registrations.append(new_registration)
        return {
            "message": "Registration successful",
            "registration": new_registration
        }

    @staticmethod
    def get_registrations():
        return {
            "message": "All registrations retrieved",
            "registrations": registrations
        }

    @staticmethod
    def get_registration_by_id(registration_id: str):
        registration = next((reg for reg in registrations if reg.id == registration_id), None)
        if not registration:
            raise HTTPException(status_code=404, detail="Registration not found")
        return {
            "message": f"Registration {registration_id} found",
            "registration": registration
        }

    @staticmethod
    def mark_attendance(registration_id: str):
        registration = next((reg for reg in registrations if reg.id == registration_id), None)
        if not registration:
            raise HTTPException(status_code=404, detail="Registration not found")

        registration.attended = True
        return {
            "message": f"Attendance marked for registration {registration_id}",
            "registration": registration
        }


registration_service = RegistrationService()
