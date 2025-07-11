from schemas.user import UserCreate, UserUpdate
from database import users
from model import User as UserModel
# import uuid  # Uncomment if switching to UUIDs


class UserService:

    @staticmethod
    def create_user(user_data: UserCreate):
        new_user = UserModel(
            id=len(users) + 1,  # Replace with str(uuid.uuid4()) for UUIDs
            name=user_data.name,
            email=user_data.email,
            is_active=True
        )
        users.append(new_user)
        return {
            "message": "User created successfully",
            "user": new_user
        }

    @staticmethod
    def get_users():
        return {
            "message": "List of all users",
            "users": users
        }

    @staticmethod
    def get_user_by_id(user_id: int):
        user = next((u for u in users if u.id == user_id), None)
        if user:
            return {
                "message": f"User {user_id} found",
                "user": user
