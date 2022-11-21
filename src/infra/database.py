from os import getenv

from dotenv import find_dotenv, load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

load_dotenv(find_dotenv())
DB_HOST: str = getenv("DB_HOST")
DB_DATABASE: str = getenv("DB_DATABASE")
DB_USER: str = getenv("DB_USER")
DB_PASSWORD: str = getenv("DB_PASSWORD")

SQLALCHEMY_DATABASE_URL: str = (
    f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_DATABASE}"
)
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


def get_db() -> None:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
