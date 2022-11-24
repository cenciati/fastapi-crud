from fastapi import status
from fastapi.responses import Response
from fastapi.testclient import TestClient

from src.core.http_server import app

client = TestClient(app)
response: Response = client.get("/")


def test_if_status_code_is_equal_to_200_when_make_get_request() -> None:
    assert response.status_code == status.HTTP_200_OK


def test_response_welcome_message() -> None:
    assert response.json()["data"] == ["Welcome to my personal blog!"]
