from typing import List, Sequence

from fastapi import HTTPException, status

from src.data import schemas


def check_if_posts_exist(posts: Sequence[schemas.Post]) -> None:
    if not posts:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Could not find any post.",
        )
    return None


def check_if_post_exists(post: List[schemas.Post]) -> None:
    if not post:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Could not find post with id {post[0].id}.",
        )
    return None


def check_duplicate_post(post: List[schemas.Post]) -> None:
    if post:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=f"Post with id {post[0].id} already exists.",
        )
    return None
