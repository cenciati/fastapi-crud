from datetime import datetime

from pydantic import BaseModel, EmailStr


class Post(BaseModel):
    id: int
    author: str
    title: str
    content: str
    created_at: datetime


class User(BaseModel):
    id: int
    email: EmailStr
    password: str
    created_at: datetime
