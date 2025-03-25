import os

from fastapi import APIRouter,Depends

from api.db.session import get_session
from sqlmodel import Session

from .models import EventModel, EventListSchema, EventCreateSchema, EventUpdateSchema

router = APIRouter()
from api.db.config import DATABASE_URL

#GET /events/
@router.get("/")
def read_events() -> EventListSchema:
    #return a bunch of events
    print(os.environ.get("DATABASE_URL"),DATABASE_URL)
    return {
        "results": [{"id":1},{"id":2},{"id":3}]
        }

#POST /events/
@router.post("/", response_model=EventModel)
def create_event(
    payload:EventCreateSchema, session: Session = Depends(get_session)):
    #return a bunch of events
    data=payload.model_dump()
    obj=EventModel.model_validate(data)
    session.add(obj)
    session.commit()
    session.refresh(obj)
    return {
         "id": 123, **data
        }

#GET /events/{event_id}
@router.get("/{event_id}")
def read_event(event_id: int) -> EventModel:
    #return a single event
    return {
        "id": event_id
        }

#PUT /events/{event_id}
@router.put("/{event_id}")
def update_event(event_id: int, payload:EventUpdateSchema) -> EventModel:
    #return a single event
    print(payload.description)
    return {
        "id": event_id, "description": payload.description
        }

#DELETE /events/{event_id}
@router.delete("/{event_id}")
def remove_event(event_id: int, payload:dict = {}) -> EventModel:
    #return a single event
    return {
        "id": event_id
        }
