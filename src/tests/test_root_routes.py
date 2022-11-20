from fastapi import status
from fastapi.responses import Response
from fastapi.testclient import TestClient

from src.routes.root_routes import root_routes

client = TestClient(root_routes)
url: str = "https://localhost:8000/api/v1/"
response: Response = client.get(f"{url}")


def test_if_status_code_is_equal_to_200_when_make_get_request() -> None:
    assert response.status_code == status.HTTP_200_OK


def test_response_data() -> None:
    assert response.json()["data"] == ["Welcome to my personal blog!"]
