from fastapi import APIRouter, HTTPException
from schemas.user import UserCreate, UserUpdate
from services.user import user_service

user_router = APIRouter()

@user_router.post("/", status_code=201)
def create_user(user_data: UserCreate):
  user = user_service.create_user(user_data)
  return {"message": "User added successfully", "user": user}


@user_router.get("/", status_code=200)
def get_users():
  return user_service.get_users()


@user_router.get("/{user_id}", status_code=200)
def get_user_by_id(user_id: int):
  # return user_service.get_user_by_id(user_id)
  user = user_service.get_user_by_id(user_id)
  if not user:
    raise HTTPException(status_code=404, detail="User not found.")
  return user

@user_router.put("/{user_id}", status_code=200)
def update_user(user_id: int, user_data: UserUpdate):
  user = user_service.update_user(user_id, user_data)
  if not user:
    raise HTTPException(status_code=404, detail="User not found")
  return {"message": "User updated successfully", "user": user}

@user_router.post("/{user_id}/deactivate")
def deactivate_user(user_id: int):
  user = user_service.deactivate_user(user_id)
  if not user:
    raise HTTPException(status_code=404, detail="User not found")
  return {"message": "User deactivated successfully", "user": user}


@user_router.delete("/{user_id}")
def delete_user(user_id: int):
  is_deleted = user_service.delete_user(user_id)
  if not is_deleted:
    raise HTTPException(status_code=404, detail=f"User with id: {user_id} not found")
  return {"Message": "User deleted successfully"}