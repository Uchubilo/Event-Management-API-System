class User: 
  def __init__(self, id: int, name: str, email: str, is_active: bool = True):
    self.id = id
    self.name = name
    self.email = email
    self.is_active = is_active


class Event:
  def __init__(self, id: int, title: str, location: str, date: str, is_open: bool = True):
    self.id = id
    self.title = title
    self.location = location
    self.date = date
    # self.event_created_at = date  # Assuming date is a string in the format 'YYYY-MM-DD'
    self.is_open = is_open


class Speaker:
  def __init__(self, id: int, name: str, topic: str):
    self.id = id
    self.name = name
    self.topic = topic


class Registration:
  def __init__(self, id: str, user_id: int, event_id: int, registration_date: str, attended: bool = False):
    self.id = id
    self.user_id = user_id
    self.event_id = event_id
    self.registration_date = registration_date
    self.attended = attended