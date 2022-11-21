from sqlalchemy import TIMESTAMP, Column, Integer, String
from sqlalchemy.sql.expression import text

from src.infra.database import Base


class Posts(Base):
    __tablename__ = "posts"

    id = Column(Integer, primary_key=True, nullable=False)
    author = Column(String, nullable=False)
    title = Column(String, nullable=False)
    content = Column(String, nullable=False)
    created_at = Column(
        TIMESTAMP(timezone=False), nullable=False, server_default=text("now()")
    )


class Users(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, nullable=False)
    email = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)
    created_at = Column(
        TIMESTAMP(timezone=False), nullable=False, server_default=text("now()")
    )
