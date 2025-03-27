import sqlmodel
from sqlmodel import SQLModel, Session
from .config import DATABASE_URL, DB_Timezone
import timescaledb

if DATABASE_URL =="":
    raise NotImplementedError("DATABASE_URL is not set")


engine=timescaledb.create_engine(DATABASE_URL,timezone=DB_Timezone)

def init_db():
    print("Creating db")
    SQLModel.metadata.create_all(engine)
    print("Creating hypertables")
    timescaledb.metadata.create_all(engine)
    print("Done")
    

def get_session():
    with Session(engine) as session:
        yield session
