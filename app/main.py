from typing import Optional, List
from fastapi import FastAPI
from models import User, Gender, Role
from uuid import uuid4, UUID

app = FastAPI()


db: List[User] = [
    User(
        id=UUID("eef76fe8-8099-4adb-86b8-86425bb2ecf7"),
        first_name="jamila",
        last_name="Ahmed",
        gender=Gender.female,
        roles=[Role.student]
        ),
    User(
        id=UUID("598fbc21-52f7-4c19-8141-b8cf9421efeb"),
        first_name="Alex",
        last_name="Jones",
        gender=Gender.male,
        roles=[Role.admin, Role.user]
        )
]

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/api/v1/users")
async def fetch_users():
    return db;

@app.post("/api/v1/users")
async def register_user(user: User):
    db.append(user)
    return {"id": user.id}