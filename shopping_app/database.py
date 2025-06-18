from fastapi import Depends, FastAPI, HTTPException, Query
from sqlmodel import Field, Session, SQLModel, create_engine, select
from typing import Annotated
from urllib.parse import quote_plus


MYSQL_USER = "root"
MYSQL_PASSWORD = quote_plus("Tomy@28728283701920")
MYSQL_HOST = "localhost"
MYSQL_DB = "Myshop"

mysql_url = f"mysql+pymysql://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_HOST}/{MYSQL_DB}"
engine = create_engine(mysql_url, echo=True)

def create_db():
    SQLModel.metadata.create_all(engine)

def get_session():
    with Session(engine) as session:
        yield session

SessionDep = Annotated[Session, Depends(get_session)]