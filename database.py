# Import the data models for use in memory-based storage
from model import User, Event, Speaker, Registration

# In-memory list to store all registered users
users: list[User] = []

# In-memory list to store all created events
events: list[Event] = []

# Predefined list of speakers available for events
speakers: list[Speaker] = [
    Speaker(id=1, name="Alice Johnson", topic="Tech Innovation"),
    Speaker(id=2, name="Bob Smith", topic="Leadership"),
    Speaker(id=3, name="Carol Davis", topic="Sustainability")
]

# In-memory list to track all event registrations
registrations: list[Registration] = []
