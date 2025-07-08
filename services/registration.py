from fastapi import HTTPException
from schemas.registration import RegistrationBase
from database import registrations
from model import Registration as RegistrationModel
from services.user import user_service
from services.event import event_service
from model import Registration as RegistrationModel
import uuid 


class RegistrationService:
  @staticmethod
  def create_registration(registration_data: RegistrationBase):
    user = user_service.get_user_by_id(registration_data.user_id)
    if not user:
      raise HTTPException(status_code=404, detail="Invalid user ID")
    if not user.is_active:
      raise HTTPException(status_code=400, detail="User is not active")
    
    event = event_service.get_event(registration_data.event_id)
    if not event:
      raise HTTPException(status_code=404, detail="Invalid event ID")
    if not event.is_open:
      raise HTTPException(status_code=400, detail="Event is not open for registration")
    
    for registration in registrations:
      if registration.user_id == registration_data.user_id and registration.event_id == registration_data.event_id:
        raise HTTPException(status_code=400, detail="User already registered for this event")
      
    new_registration = RegistrationModel(
      # id=len(registrations) + 1,
      id = str(uuid.uuid4()),
      user_id=registration_data.user_id,
      event_id=registration_data.event_id,
      registration_date=registration_data.registration_date,
      attended=False
    )
    registrations.append(new_registration)
    return new_registration
  
  @staticmethod
  def get_registrations():
    return registrations
  
  @staticmethod
  def get_registration_by_id(registration_id: str):
    for registration in registrations:
      if registration.id == registration_id:
        return registration
    return None
    
  @staticmethod
  def mark_attendance(registration_id: str):
    registration = RegistrationService.get_registration_by_id(registration_id)
    if not registration:
      raise HTTPException(status_code=404, detail="Registration not found")
    
    registration.attended = True
    return registration

    
registration_service = RegistrationService()