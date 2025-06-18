from typing import Optional
from pydantic import BaseModel

class UserCreate(BaseModel):
    username: str
    email: str
    password: str

class UserOut(BaseModel):
    id: int
    username: str
    email: str
    is_active: bool

    class Config:
        orm_mode = True

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: Optional[str] = None

class ProductCreate(BaseModel):
    name: str
    price: float
    brand: str
    on_sale: Optional[bool] = False
    exp_date: Optional[str] = None

class ProductOut(ProductCreate):
    id: int

    class Config:
        orm_mode = True
