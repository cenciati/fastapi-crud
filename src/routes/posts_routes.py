from typing import Dict, Union

from fastapi import APIRouter, status
from fastapi.encoders import jsonable_encoder

from src.core.config import settings
from src.data import schemas
from src.data.posts_data import (
    delete_post_by_id,
    fetch_all_posts,
    fetch_post_by_id,
    insert_post,
    update_post_by_id,
)
from src.services.posts_services import (
    check_if_post_exists,
    check_if_posts_exist,
    check_duplicate_post,
)

posts_router = APIRouter(prefix="/posts")


@posts_router.get("/", status_code=status.HTTP_200_OK, response_model=dict)
async def get_all_posts() -> Dict[str, Union[list, dict]]:
    posts: list = fetch_all_posts()
    check_if_posts_exist(posts)
    return {
        "data": jsonable_encoder(posts),
        "_links": {
            "self": {"href": f"{settings.URL}/posts"},
            "root": {"href": f"{settings.URL}/"},
        },
    }


@posts_router.get("/{id}", status_code=status.HTTP_200_OK, response_model=dict)
async def get_one_post_by_id(id: int) -> Dict[str, Union[list, dict]]:
    post: list = fetch_post_by_id(id)
    check_if_post_exists(post)
    return {
        "data": jsonable_encoder([post]),
        "_links": {
            "self": {"href": f"{settings.URL}/posts/{id}"},
            "root": {"href": f"{settings.URL}/"},
        },
    }


@posts_router.post(
    "/", status_code=status.HTTP_201_CREATED, response_model=dict
)
async def create_post(new_post: schemas.Post) -> Dict[str, Union[list, dict]]:
    post: list = fetch_post_by_id(new_post.id)
    check_duplicate_post(post)
    insert_post(new_post)
    return {
        "data": jsonable_encoder([new_post]),
        "_links": {
            "self": {"href": f"{settings.URL}/posts"},
            "root": {"href": f"{settings.URL}/"},
        },
    }


@posts_router.delete(
    "/{id}",
    status_code=status.HTTP_204_NO_CONTENT,
    response_model=None,
)
async def delete_post(id: int) -> None:
    post: list = fetch_post_by_id(id)
    check_if_post_exists(post)
    delete_post_by_id(id)
    return None


@posts_router.put("/{id}", status_code=status.HTTP_200_OK, response_model=dict)
async def update_post(
    id: int, updated_post: schemas.Post
) -> Dict[str, Union[list, dict]]:
    post: list = fetch_post_by_id(id)
    check_if_post_exists(post)
    update_post_by_id(updated_post)
    return {
        "data": jsonable_encoder([updated_post]),
        "_links": {
            "self": {"href": f"{settings.URL}/posts/{id}"},
            "root": {"href": f"{settings.URL}/"},
        },
    }
