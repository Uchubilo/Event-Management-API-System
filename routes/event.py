from fastapi import APIRouter, HTTPException
from schemas.event import EventCreate, EventUpdate
from services.event import event_service

event_router = APIRouter(prefix="/events", tags=["Events"])


@event_router.post("/", status_code=201)
def create_event(event_data: EventCreate):
    result = event_service.create_event(event_data)
    return {
        "message": "Event created successfully",
        "event": result.get("event"),
        "speakers": result.get("speakers")
    }


@event_router.get("/", status_code=200)
def get_events():
    result = event_service.get_events()
    return {
        "message": "List of all events",
        "events": result.get("events")
    }


@event_router.get("/{event_id}", status_code=200)
def get_event(event_id: int):
    result = event_service.get_event(event_id)
    if not result or not result.get("event"):
        raise HTTPException(status_code=404, detail=f"Event with ID {event_id} not found.")
    return result


@event_router.put("/{event_id}", status_code=200)
def update_event(event_id: int, event_data: EventUpdate):
    result = event_service.update_event(event_id, event_data)
    if not result or not result.get("event"):
        raise HTTPException(status_code=404, detail=f"Event with ID {event_id} not found.")
    return {
        "message": "Event updated successfully",
        "event": result.get("event")
    }


@event_router.post("/{event_id}/close", status_code=200)
def close_event(event_id: int):
    result = event_service.close_event(event_id)
    if not result or not result.get("event"):
        raise HTTPException(status_code=404, detail=f"Event with ID {event_id} not found.")
    return {
        "message": "Event closed successfully",
        "event": result.get("event")
    }


@event_router.delete("/{event_id}", status_code=200)
def delete_event(event_id: int):
    result = event_service.delete_event(event_id)
    if not result.get("deleted"):
        raise HTTPException(status_code=404, detail=f"Event with ID {event_id} not found.")
    return {"message": "Event deleted successfully"}
