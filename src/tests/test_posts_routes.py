from fastapi import status
from fastapi.testclient import TestClient

from src.core.config import settings
from src.core.http_server import app
from src.data import schemas
from src.data.schemas import Post

client = TestClient(app)
url: str = f"{settings.URL}/posts"
post: schemas.Post = Post(
    id=99,
    author="Mark",
    title="How to use Unity.",
    content="In this tutorial...",
)


# POST /api/v1/posts
def test_if_status_code_is_equal_201_when_create_a_post() -> None:
    response = client.post(url, json=post.dict())
    assert response.status_code == status.HTTP_201_CREATED


# GET /api/v1/posts
def test_if_status_code_is_equal_200_when_get_all_posts() -> None:
    response = client.get(url)
    assert response.status_code == status.HTTP_200_OK


# GET /api/v1/posts/{id}
def test_if_status_code_is_equal_200_when_get_one_post() -> None:
    response = client.get(f"{url}/{post.id}")
    assert response.status_code == status.HTTP_200_OK


# PUT /api/v1/posts/{id}
def test_if_status_code_is_equal_200_when_update_a_post() -> None:
    updated_post: schemas.Post = Post(
        id=post.id,
        author="Edited author",
        title="Edited title",
        content="Edited content",
    )
    response = client.put(f"{url}/{post.id}", json=updated_post.dict())
    assert response.status_code == status.HTTP_200_OK


# DELETE /api/v1/posts/{id}
def test_if_status_code_is_equal_204_when_delete_a_post() -> None:
    response = client.delete(f"{url}/{post.id}")
    assert response.status_code == status.HTTP_204_NO_CONTENT
