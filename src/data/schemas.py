from pydantic import BaseModel, EmailStr


class Post(BaseModel):
    id: int
    author: str
    title: str
    content: str


class User(BaseModel):
    id: int
    email: EmailStr
    password: str
