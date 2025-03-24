from fastapi import APIRouter
from .schema import EventSchema, EventListSchema

router = APIRouter()

@router.get("/")
def read_events() -> EventListSchema:
    #return a bunch of events
    return {
        "results": [{"id":1},{"id":2},{"id":3}]
        }


@router.get("/{event_id}")
def read_event(event_id: int) -> EventSchema:
    #return a single event
    return {
        "id": event_id
        }
