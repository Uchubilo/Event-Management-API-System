from pydantic import BaseModel, Field
from datetime import date


class RegistrationBase(BaseModel):
    user_id: int = Field(..., example=1)
    event_id: int = Field(..., example=101)
    registration_date: date = Field(..., example="2025-07-15")


class RegistrationCreate(RegistrationBase):
    """Schema for creating a new registration."""
    pass


class Registration(RegistrationCreate):
    """Full registration model, including ID and attendance status."""
    id: str = Field(..., example="a1b2c3d4-e5f6-7890-abcd-1234567890ef")
    attended: bool = Field(default=False, example=False)


class TrackAttendance(BaseModel):
    """Schema for updating attendance status."""
    attended: bool = Field(default=True, example=True)
