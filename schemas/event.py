from pydantic import BaseModel, Field
from typing import Optional
from datetime import date


class EventBase(BaseModel):
    title: str = Field(..., example="Tech Conference 2025")
    location: str = Field(..., example="Lagos, Nigeria")
    event_date: date = Field(..., example="2025-09-15")


class EventCreate(EventBase):
    """Schema for creating a new event."""
    pass


class Event(EventBase):
    """Full event representation (e.g., returned to clients)."""
    id: int
    is_open: bool = True


class EventUpdate(BaseModel):
    """Schema for partial event updates."""
    title: Optional[str] = Field(None, example="Updated Conference Title")
    location: Optional[str] = Field(None, example="Abuja, Nigeria")
    event_date: Optional[date] = Field(None, example="2025-10-01")
