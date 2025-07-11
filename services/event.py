from schemas.event import EventCreate, EventUpdate
from database import events, speakers
from model import Event as EventModel


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
        return {
            "message": "Event created successfully",
            "event": new_event,
            "speakers": speakers
        }

    @staticmethod
    def get_events():
        return {
            "message": "List of all events",
            "events": events
        }

    @staticmethod
    def get_event(event_id: int):
        event = next((e for e in events if e.id == event_id), None)
        if event:
            return {
                "message": f"Event {event_id} found",
                "event": event
            }
        return {
            "message": f"Event {event_id} not found",
            "event": None
        }

    @staticmethod
    def update_event(event_id: int, event_data: EventUpdate):
        event = next((e for e in events if e.id == event_id), None)
        if not event:
            return {
                "message": f"Event {event_id} not found",
                "event": None
            }
        event.title = event_data.title
        event.location = event_data.location
        event.date = event_data.event_date
        return {
            "message": f"Event {event_id} updated successfully",
            "event": event
        }

    @staticmethod
    def close_event(event_id: int):
        event = next((e for e in events if e.id == event_id), None)
        if not event:
            return {
                "message": f"Event {event_id} not found",
                "event": None
            }
        event.is_open = False
        return {
            "message": f"Event {event_id} closed",
            "event": event
        }

    @staticmethod
    def delete_event(event_id: int):
        event = next((e for e in events if e.id == event_id), None)
        if not event:
            return {
                "message": f"Event {event_id} not found",
                "deleted": False
            }
        events.remove(event)
        return {
            "message": f"Event {event_id} deleted successfully",
            "deleted": True
        }


event_service = EventService()
