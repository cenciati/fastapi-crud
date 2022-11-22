import pytest
from fastapi import HTTPException, status

from src.services.posts_services import (
    check_if_post_exists,
    check_if_posts_exist,
)


def test_if_it_raises_an_http_exception_when_sent_empty_list_of_posts() -> None:
    posts = []
    with pytest.raises(HTTPException):
        check_if_posts_exist(posts=posts)
        assert True


def test_if_status_code_is_equal_to_404_when_it_raises_an_http_exception_for_empty_list_of_posts() -> None:
    posts = []
    with pytest.raises(HTTPException) as error:
        check_if_posts_exist(posts=posts)

    assert error.value.status_code == status.HTTP_404_NOT_FOUND


def test_error_message_when_it_raises_an_http_exception_for_empty_list_of_posts() -> None:
    posts = []
    with pytest.raises(HTTPException) as error:
        check_if_posts_exist(posts=posts)

    assert error.value.detail == "Could not find any post."


def test_if_it_raises_an_http_exception_when_sent_empty_post() -> None:
    post = []
    with pytest.raises(HTTPException):
        check_if_post_exists(id=99, post=post)
        assert True


def test_if_status_code_is_equal_to_404_when_it_raises_an_http_exception_for_empty_post() -> None:
    post = []
    with pytest.raises(HTTPException) as error:
        check_if_post_exists(id=99, post=post)

    assert error.value.status_code == status.HTTP_404_NOT_FOUND


def test_error_message_when_it_raises_an_http_exception_for_empty_post() -> None:
    post = []
    with pytest.raises(HTTPException) as error:
        check_if_post_exists(id=99, post=post)

    assert error.value.detail == "Could not find post with id 99."
