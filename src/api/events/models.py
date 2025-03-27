#from pydantic import BaseModel
from datetime import datetime,timezone
from typing import List, Optional
from sqlmodel import SQLModel, Field
import sqlmodel
from timescaledb import TimescaleModel

def get_utcnow():
    return datetime.now(timezone.utc).replace(tzinfo=timezone.utc)



class EventModel(TimescaleModel, table=True):
    #id: Optional[int] = Field(default=None, primary_key=True)

    page: str = Field(index=True)
    description: Optional[str] = ""
    # created_at: datetime = Field(
    #     default_factory=get_utcnow,
    #     sa_type=sqlmodel.DateTime(timezone=True),
    #     nullable=False
    # )
    updated_at: datetime = Field(
        default_factory=get_utcnow,
        sa_type=sqlmodel.DateTime(timezone=True),
        nullable=False
    )

    __chunk_time_interval__="INTERVAL 1 day"
    __drop_after__="INTERVAL 1 month"


class EventCreateSchema(SQLModel):
    page: str
    description: Optional[str] = Field(default=None)

class EventUpdateSchema(SQLModel):
    description: str

class EventListSchema(SQLModel):
    results: List[EventModel]

class EventBucketSchema(SQLModel):
    bucket: datetime
    page: str
    count: int