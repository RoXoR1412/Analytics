from fastapi import APIRouter
from .schema import EventSchema

router = APIRouter()

@router.get("/")
def read_events():
    #return a bunch of events
    return {
        "items": [1,2,3]
        }


@router.get("/{event_id}")
def read_event(event_id: int) -> EventSchema:
    #return a single event
    return {
        "id": event_id
        }
