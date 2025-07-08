from schemas.event import EventCreate, EventUpdate
from database import events
from model import Event as EventModel
from database import speakers

class EventService:

  @staticmethod
  def create_event(event_data: EventCreate):
    new_event = EventModel(
      id=len(events) + 1,
      title=event_data.title,
      location=event_data.location,
      date=event_data.event_date,
      is_open=True
    )
    events.append(new_event)
    
    return {"event": new_event, "speakers": speakers}

  @staticmethod
  def get_events():
    return {"events": events}
  
  @staticmethod
  def get_event(event_id: int):
    for event in events:
      if event.id == event_id:
        return event
    return None
  
  @staticmethod
  def update_event(event_id: int, event_data: EventUpdate):
    for event in events:
      if event.id == event_id:
        event.title = event_data.title
        event.location = event_data.location
        event.date = event_data.event_date
        return event
    return None
  
  @staticmethod
  def close_event(event_id: int):
    for event in events:
      if event.id == event_id:
        event.is_open = False
        return event
    return None
  

  @staticmethod
  def delete_event(event_id: int):
    for event in events:
      if event.id == event_id:
        events.remove(event)
        return True
    return False


event_service = EventService()