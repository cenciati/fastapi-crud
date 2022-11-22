from typing import Optional

from fastapi import HTTPException, status

from src.data import schemas


def check_if_posts_exist(posts: Optional[schemas.Post] = None) -> None:
    if not posts:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Could not find any post.",
        )
    return None


def check_if_post_exists(
    id: Optional[int] = None, post: Optional[schemas.Post] = None
) -> None:
    if id and not post:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Could not find post with id {id}.",
        )
    return None
