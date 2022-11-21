from datetime import datetime
from json import dumps

from fastapi import status
from fastapi.testclient import TestClient

from data.schemas import Post
from src.routes.posts_routes import posts_routes

client = TestClient(posts_routes)
url: str = "http://localhost:8000/api/v1/posts"
post: Post = Post(
    id=1,
    author="Mark",
    title="How to use Unity.",
    content="In this tutorial...",
    created_at=datetime.now(),
)


# POST /api/v1/posts
def test_if_status_code_is_equal_201_when_create_a_post() -> None:
    response = client.post(f"{url}", data=dumps(post.dict()))
    assert response.status_code == status.HTTP_201_CREATED


# GET /api/v1/posts
def test_if_status_code_is_equal_200_when_get_all_posts() -> None:
    response = client.get(f"{url}")
    assert response.status_code == status.HTTP_200_OK


# GET /api/v1/posts/{id}
def test_if_status_code_is_equal_200_when_get_one_post() -> None:
    response = client.get(f"{url}/{1}")
    assert response.status_code == status.HTTP_200_OK


# PUT /api/v1/posts/{id}
def test_if_status_code_is_equal_200_when_update_a_post() -> None:
    updated_post: Post = Post(
        id=1,
        author="Edited author",
        title="Edited title",
        content="Edited content",
    )
    response = client.put(f"{url}/{1}", data=dumps(updated_post.dict()))
    assert response.status_code == status.HTTP_200_OK


# DELETE /api/v1/posts/{id}
def test_if_status_code_is_equal_204_when_delete_a_post() -> None:
    response = client.delete(f"{url}/{1}")
    assert response.status_code == status.HTTP_204_NO_CONTENT
