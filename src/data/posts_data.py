from sqlalchemy.orm import Session

from src.data import schemas
from src.infra import models
from src.infra.database import engine, get_db

models.Base.metadata.create_all(bind=engine)
db: Session = next(get_db())


def fetch_all_posts() -> list:
    posts = db.query(models.Posts).all()
    return posts


def fetch_post_by_id(id: int) -> list:
    post = db.query(models.Posts).filter(models.Posts.id == id).first()
    return post


def insert_post(post: schemas.Post) -> None:
    new_post = models.Posts(**post.dict())
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return None


def delete_post_by_id(id: int) -> None:
    db.query(models.Posts).filter(models.Posts.id == id).delete(
        synchronize_session=False
    )
    db.commit()
    return None


def update_post_by_id(post: schemas.Post) -> None:
    db.query(models.Posts).filter(models.Posts.id == post.id).update(
        post.dict(), synchronize_session=False
    )
    db.commit()
    return None
