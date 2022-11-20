from typing import Optional

from pydantic import BaseModel


class Post(BaseModel):
    id: int
    author: Optional[str] = "Anonymous"
    title: str
    content: str
