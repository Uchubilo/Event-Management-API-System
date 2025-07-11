from pydantic import BaseModel, Field, EmailStr
from typing import Optional


class UserBase(BaseModel):
    name: str = Field(..., example="Jane Doe")
    email: EmailStr = Field(..., example="jane.doe@example.com")


class UserCreate(UserBase):
    """Schema for creating a new user."""
    pass


class User(UserBase):
    """Full user model with ID and activation status."""
    id: int = Field(..., example=1)
    is_active: bool = Field(default=False, example=True)


class UserUpdate(BaseModel):
    """Schema for updating user details (partial update)."""
    name: Optional[str] = Field(None, example="John Smith")
    email: Optional[EmailStr] = Field(None, example="john.smith@example.com")

