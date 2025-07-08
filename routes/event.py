from fastapi import APIRouter, HTTPException
from schemas.event import EventCreate, EventUpdate
from services.event import event_service 

event_router = APIRouter()

@event_router.post("/", status_code=201)
def create_event(event_data: EventCreate):
  event = event_service.create_event(event_data)
  return {"message": "Event created successfully", "event_details": event}


@event_router.get("/", status_code=200)
def get_events():
  event = event_service.get_events()
  return {"events": event["events"]}


@event_router.get("/{event_id}", status_code=200)
def get_event(event_id: int):
  # return user_service.get_user_by_id(user_id)
  event = event_service.get_event(event_id)
  if not event:
    raise HTTPException(status_code=404, detail="User not found.")
  return event

@event_router.put("/{event_id}", status_code=200)
def update_event(event_id: int, event_data: EventUpdate):
  event = event_service.update_event(event_id, event_data)
  if not event:
    raise HTTPException(status_code=404, detail="Event not found")
  return {"message": "Event updated successfully", "event": event}

@event_router.post("/{event_id}/close", status_code=200)
def close_event(event_id: int):
  event = event_service.close_event(event_id)
  if not event:
    raise HTTPException(status_code=404, detail="Event not found")
  return {"message": "Event closed successfully", "event": event}

@event_router.delete("/{event_id}")
def delete_event(event_id: int):
  is_deleted = event_service.delete_event(event_id)
  if not is_deleted:
    raise HTTPException(status_code=404, detail=f"Event with id: {event_id} not found")
  return {"Message": "Event deleted successfully"}