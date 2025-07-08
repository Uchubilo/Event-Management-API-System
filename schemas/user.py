from pydantic import BaseModel
from typing import Optional

class UserBase(BaseModel):
  name: str
  email: str

class UserCreate(UserBase):
  pass

class User(UserCreate):
  id: int
  is_active: bool = False

class UserUpdate(BaseModel):
  name: Optional[str] = None
  email: Optional[str] = None
