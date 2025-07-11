from fastapi import APIRouter, HTTPException
from schemas.user import UserCreate, UserUpdate
from services.user import user_service

user_router = APIRouter(prefix="/users", tags=["Users"])


@user_router.post("/", status_code=201)
def create_user(user_data: UserCreate):
    result = user_service.create_user(user_data)
    return {
        "message": "User added successfully",
        "user": result.get("user") if isinstance(result, dict) else result
    }


@user_router.get("/", status_code=200)
def get_users():
    result = user_service.get_users()
    return {
        "message": "List of all users",
        "users": result.get("users") if isinstance(result, dict) else result
    }


@user_router.get("/{user_id}", status_code=200)
def get_user_by_id(user_id: int):
    result = user_service.get_user_by_id(user_id)
    user = result.get("user") if isinstance(result, dict) else result
    if not user:
        raise HTTPException(status_code=404, detail=f"User with ID {user_id} not found.")
    return result


@user_router.put("/{user_id}", status_code=200)
def update_user(user_id: int, user_data: UserUpdate):
    result = user_service.update_user(user_id, user_data)
    user = result.get("user") if isinstance(result, dict) else result
    if not user:
        raise HTTPException(status_code=404, detail=f"User with ID {user_id} not found.")
    return {
        "message": "User updated successfully",
        "user": user
    }


@user_router.post("/{user_id}/deactivate", status_code=200)
def deactivate_user(user_id: int):
    result = user_service.deactivate_user(user_id)
    user = result.get("user") if isinstance(result, dict) else result
    if not user:
        raise HTTPException(status_code=404, detail=f"User with ID {user_id} not found.")
    return {
        "message": "User deactivated successfully",
        "user": user
    }


@user_router.delete("/{user_id}", status_code=200)
def delete_user(user_id: int):
    result = user_service.delete_user(user_id)
    deleted = result.get("deleted") if isinstance(result, dict) else result
    if not deleted:
        raise HTTPException(status_code=404, detail=f"User with ID {user_id} not found.")
    return {
        "message": "User deleted successfully"
    }
