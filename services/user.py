from schemas.user import UserCreate, UserUpdate
from database import users
from model import User as UserModel
# import uuid

class UserService:

  @staticmethod
  def create_user(user_data: UserCreate):
    new_user = UserModel(
      id=len(users) + 1,
      # id = str(uuid.uuid4()),  # Assuming you want to use UUIDs for user IDs
      name=user_data.name,
      email=user_data.email,
      is_active=True
    )
    users.append(new_user)
    return new_user
  

  @staticmethod
  def get_users():
    return users
  
  @staticmethod
  def get_user_by_id(user_id: int):
    for user in users:
      if user.id == user_id:
        return user
    return None
  
  @staticmethod
  def update_user(user_id: int, user_data: UserUpdate):
    for user in users:
      if user.id == user_id:
        user.name = user_data.name
        user.email = user_data.email
        return user
    return None
  
  @staticmethod
  def deactivate_user(user_id: int):
    for user in users:
      if user.id == user_id:
        user.is_active = False
        return user
    return None

  
  @staticmethod
  def delete_user(user_id: int):
    for user in users:
      if user.id == user_id:
        users.remove(user)
        return True
    return False
  
  
user_service = UserService()