from sqlmodel import SQLModel, create_engine, Session
from typing import Generator
from urllib.parse import quote_plus
import os  
from dotenv import load_dotenv  

load_dotenv()

MYSQL_USER = os.getenv("MYSQL_USER", "root")
MYSQL_PASSWORD = quote_plus(os.getenv("MYSQL_PASSWORD"))
MYSQL_HOST = os.getenv("MYSQL_HOST")
MYSQL_DB = os.getenv("MYSQL_DB")

DATABASE_URL = f"mysql+pymysql://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_HOST}/{MYSQL_DB}"
engine = create_engine(DATABASE_URL, echo=True)

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

def get_session() -> Generator[Session, None, None]:
    with Session(engine) as session:
        yield session