# Import the data models for use in memory-based storage
from model import User, Event, Speaker, Registration

# In-memory list to store all registered users
users: list[User] = []

# In-memory list to store all created events
events: list[Event] = []

# Predefined list of speakers available for events
speakers: list[Speaker] = [
    Speaker(id=1, name="Emmily Doe", topic="Self Growth"),
    Speaker(id=2, name="Kindness Jig", topic="Data Extraction"),
    Speaker(id=3, name="Princess Son", topic="Geology")
]

# In-memory list to track all event registrations
registrations: list[Registration] = []
