
# Represents a user in the system
class User: 
    def __init__(self, id: int, name: str, email: str, is_active: bool = True):
        self.id = id                        # Unique identifier for the user
        self.name = name                    # Full name of the user
        self.email = email                  # Email address of the user
        self.is_active = is_active          # Status to indicate if the user is active (default: True)


# Represents an event in the system
class Event:
    def __init__(self, id: int, title: str, location: str, date: str, is_open: bool = True):
        self.id = id                        # Unique identifier for the event
        self.title = title                  # Title or name of the event
        self.location = location            # Venue or location of the event
        self.date = date                    # Date of the event in string format (e.g., 'YYYY-MM-DD')
        self.is_open = is_open              # Indicates if registration for the event is still open (default: True)


# Represents a speaker assigned to an event
class Speaker:
    def __init__(self, id: int, name: str, topic: str):
        self.id = id                        # Unique identifier for the speaker
        self.name = name                    # Name of the speaker
        self.topic = topic                  # Topic the speaker will cover at the event


# Represents a user's registration for an event
class Registration:
    def __init__(self, id: str, user_id: int, event_id: int, registration_date: str, attended: bool = False):
        self.id = id                        # Unique registration ID (could be a UUID or custom string)
        self.user_id = user_id              # ID of the registered user
        self.event_id = event_id            # ID of the event the user is registered for
        self.registration_date = registration_date  # Date when the registration was made
        self.attended = attended            # Indicates if the user attended the event (default: False)
