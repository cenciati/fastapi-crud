from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session

from src.core.config import settings
from src.data import schemas
from src.infra import models
from src.infra.database import engine, get_db
from src.services.posts_services import (
    check_if_post_exists,
    check_if_posts_exist,
)

posts_router = APIRouter()
models.Base.metadata.create_all(bind=engine)


@posts_router.get(
    "/posts", status_code=status.HTTP_200_OK, response_model=dict
)
async def get_all_posts(db: Session = Depends(get_db)) -> dict:
    posts: list = db.query(models.Posts).all()
    check_if_posts_exist(posts=posts)
    return {
        "data": jsonable_encoder(posts),
        "_links": {
            "self": {"href": f"{settings.URL}/posts"},
            "root": {"href": f"{settings.URL}/"},
        },
    }


@posts_router.get(
    "/posts/{id}", status_code=status.HTTP_200_OK, response_model=dict
)
async def get_one_post(id: int, db: Session = Depends(get_db)) -> dict:
    post = db.query(models.Posts).filter(models.Posts.id == id).first()
    check_if_post_exists(id=id, post=post)
    return {
        "data": jsonable_encoder([post]),
        "_links": {
            "self": {"href": f"{settings.URL}/posts/{id}"},
            "root": {"href": f"{settings.URL}/"},
        },
    }


@posts_router.post(
    "/posts", status_code=status.HTTP_201_CREATED, response_model=dict
)
async def create_post(
    post: schemas.Post, db: Session = Depends(get_db)
) -> dict:
    if db.query(models.Posts).filter(models.Posts.id == post.id).first():
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=f"Post with id {post.id} already exists.",
        )
    post = models.Posts(**post.dict())
    db.add(post)
    db.commit()
    db.refresh(post)
    return {
        "data": jsonable_encoder([post]),
        "_links": {
            "self": {"href": f"{settings.URL}/posts"},
            "root": {"href": f"{settings.URL}/"},
        },
    }


@posts_router.delete(
    "/posts/{id}",
    status_code=status.HTTP_204_NO_CONTENT,
    response_model=None,
)
async def delete_post(id: int, db: Session = Depends(get_db)) -> None:
    post_query = db.query(models.Posts).filter(models.Posts.id == id)
    post = post_query.first()
    check_if_post_exists(id=id, post=post)
    post_query.delete(synchronize_session=False)
    db.commit()
    return None


@posts_router.put(
    "/posts/{id}", status_code=status.HTTP_200_OK, response_model=dict
)
async def update_post(
    id: int, post: schemas.Post, db: Session = Depends(get_db)
) -> dict:
    updated_post_query = db.query(models.Posts).filter(models.Posts.id == id)
    updated_post = updated_post_query.first()
    check_if_post_exists(id=id, post=updated_post)
    updated_post_query.update(post.dict(), synchronize_session=False)
    db.commit()
    updated_post = updated_post_query.first()
    return {
        "data": jsonable_encoder([updated_post]),
        "_links": {
            "self": {"href": f"{settings.URL}/posts/{id}"},
            "root": {"href": f"{settings.URL}/"},
        },
    }


"""
GET 200
/posts?limit=10

GET 200
serach by keyword
/posts?contains=mlops
"""
