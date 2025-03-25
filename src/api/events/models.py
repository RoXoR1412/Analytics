#from pydantic import BaseModel
from typing import List, Optional
from sqlmodel import SQLModel, Field

class EventModel(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    page: Optional[str] = None
    description: Optional[str] = None


class EventCreateSchema(SQLModel):
    page: str
    description: Optional[str] = Field(default=None)

class EventUpdateSchema(SQLModel):
    description: str

class EventListSchema(SQLModel):
    results: List[EventModel]