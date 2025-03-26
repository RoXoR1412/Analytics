
from fastapi import APIRouter,Depends, HTTPException

from api.db.session import get_session
from sqlmodel import Session,select

from .models import EventModel, EventListSchema, EventCreateSchema, EventUpdateSchema

router = APIRouter()
from api.db.config import DATABASE_URL

#GET /events/
@router.get("/", response_model=EventListSchema)
def read_events(session: Session = Depends(get_session)):
    #return a bunch of events
    query=select(EventModel).order_by(EventModel.id.asc()).limit(10)
    results=session.exec(query).all()
    return {
        "results": results,
        "count": len(results)
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
@router.get("/{event_id}",response_model=EventModel)
def read_event(event_id: int,session: Session = Depends(get_session)):
    #return a single event
    query=select(EventModel).where(EventModel.id==event_id)
    result=session.exec(query).first()
    if not result:
        raise HTTPException(status_code=404,detail="Event not found")
    return {
        "id": event_id, "description": result.description, "page": result.page
        }

#PUT /events/{event_id}
@router.put("/{event_id}", response_model=EventModel)
def update_event(
    event_id: int,
    payload:EventUpdateSchema, 
    session: Session = Depends(get_session)):
    #return a single event
    query=select(EventModel).where(EventModel.id==event_id)
    obj=session.exec(query).first()
    if not obj:
        raise HTTPException(status_code=404,detail="Event not found")
    data=payload.model_dump()
    for key,value in data.items():
        setattr(obj,key,value)
    session.add(obj)
    session.commit()
    session.refresh(obj)
    return obj

#DELETE /events/{event_id}
@router.delete("/{event_id}",response_model=EventModel)
def remove_event(event_id: int, payload:dict = {},session: Session = Depends(get_session)):
    #return a single event
    query=select(EventModel).where(EventModel.id==event_id)
    obj=session.exec(query).first()
    if not obj:
        raise HTTPException(status_code=404,detail="Event not found")
    session.delete(obj)
    session.commit()
    session.refresh(obj)    
    return obj
