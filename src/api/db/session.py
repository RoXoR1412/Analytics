import sqlmodel
from sqlmodel import SQLModel, Session
from .config import DATABASE_URL

if DATABASE_URL =="":
    raise NotImplementedError("DATABASE_URL is not set")


engine=sqlmodel.create_engine(DATABASE_URL)

def init_db():
    print("Creating db")
    SQLModel.metadata.create_all(engine)


def get_session():
    with Session(engine) as session:
        yield session
