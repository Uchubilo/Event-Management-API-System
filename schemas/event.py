from pydantic import BaseModel
from typing import Optional
from datetime import date

class EventBase(BaseModel):
  title: str
  location: str
  event_date: date

class EventCreate(EventBase):
  pass

class Event(EventCreate):
  id: int
  is_open: bool = True

class EventUpdate(BaseModel):
  title: Optional[str] = None
  location: Optional[str] = None
  event_date: Optional[date] = None

