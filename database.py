from model import User, Event, Speaker, Registration

users: list[User] = []
events: list[Event] = []
speakers: list[Speaker] = [
  Speaker(id=1, name="Alice Johnson", topic="Tech Innovation"),
  Speaker(id=2, name="Bob Smith", topic="Leadership"),
  Speaker(id=3, name="Carol Davis", topic="Sustainability")
]
registrations: list[Registration] = [] 