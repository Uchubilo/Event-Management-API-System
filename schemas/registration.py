from pydantic import BaseModel
from datetime import date

class RegistrationBase(BaseModel):
  user_id: int
  event_id: int
  registration_date: date

class RegistrationCreate(RegistrationBase):
  pass

class Registration(RegistrationCreate):
  id: str
  attended: bool = False

class TrackAttendance(BaseModel):
  attended: bool = True