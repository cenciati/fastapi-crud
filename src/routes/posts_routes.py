from typing import Optional

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session

from src.data import schemas
from src.infra import models
from src.infra.database import engine, get_db

posts_routes = APIRouter()
models.Base.metadata.create_all(bind=engine)


def check_if_post_exists(
    id: Optional[int] = None, post: Optional[schemas.Post] = None
) -> None:
    # it has id but there are no data
    if id and not post:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Could not find post with id {id}.",
        )
    # it does not have id and there are no data
    if not id and not post:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Could not find any post.",
        )
    return None


@posts_routes.get(
    "/api/v1/posts", status_code=status.HTTP_200_OK, response_model=dict
)
async def get_all_posts(db: Session = Depends(get_db)) -> dict:
    posts: list = db.query(models.Posts).all()
    check_if_post_exists(post=posts)
    return {
        "data": jsonable_encoder(posts),
        "links": {"self": "/posts", "root": "/"},
    }


@posts_routes.get(
    "/api/v1/posts/{id}", status_code=status.HTTP_200_OK, response_model=dict
)
async def get_one_post(id: int, db: Session = Depends(get_db)) -> dict:
    post = db.query(models.Posts).filter(models.Posts.id == id).first()
    check_if_post_exists(id=id, post=post)
    return {
        "data": jsonable_encoder([post]),
        "links": {"self": f"/posts/{id}", "root": "/"},
    }


@posts_routes.post(
    "/api/v1/posts", status_code=status.HTTP_201_CREATED, response_model=dict
)
async def create_post(
    post: schemas.Post, db: Session = Depends(get_db)
) -> dict:
    if db.query(models.Posts).filter(models.Posts.id == post.id).first():
        return {"msg": "post already exists"}
    post = models.Posts(**post.dict())
    db.add(post)
    db.commit()
    db.refresh(post)
    return {
        "data": jsonable_encoder([post]),
        "links": {"self": "/posts", "root": "/"},
    }


@posts_routes.delete(
    "/api/v1/posts/{id}",
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


@posts_routes.put(
    "/api/v1/posts/{id}", status_code=status.HTTP_200_OK, response_model=dict
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
        "links": {"self": f"/posts/{id}", "root": "/"},
    }


"""
GET 200
/posts?limit=10

GET 200
serach by keyword
/posts?contains=mlops
"""
