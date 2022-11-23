# import pytest
# from fastapi import HTTPException, status

# from src.data.schemas import Post
# from src.services.posts_services import (
#     check_if_post_exists,
#     check_if_post_is_duplicate,
#     check_if_posts_exist,
# )


# def test_if_status_code_is_equal_to_404_when_unkown_posts_are_sent() -> None:
#     posts: list = [
#         Post(id=98, author="Test", title="Test", content="test"),
#         Post(id=99, author="Test", title="Test", content="test"),
#     ]
#     with pytest.raises(HTTPException) as error:
#         check_if_posts_exist(posts=posts)
#     assert error.value.status_code == status.HTTP_404_NOT_FOUND


# def test_error_message_when_unkown_posts_are_sent() -> None:
#     posts: list = [
#         Post(id=98, author="Test", title="Test", content="test"),
#         Post(id=99, author="Test", title="Test", content="test"),
#     ]
#     with pytest.raises(HTTPException) as error:
#         check_if_posts_exist(posts=posts)
#     assert error.value.detail == "Could not find any post."


# def test_if_status_code_is_equal_to_404_when_unkown_post_is_sent() -> None:
#     post: list = [Post(id=99, author="Test", title="Test", content="test")]
#     with pytest.raises(HTTPException) as error:
#         check_if_post_exists(post=post)
#     assert error.value.status_code == status.HTTP_404_NOT_FOUND


# def test_error_message_when_unkown_post_is_sent() -> None:
#     post: list = [Post(id=99, author="Test", title="Test", content="test")]
#     with pytest.raises(HTTPException) as error:
#         check_if_post_exists(post=post)
#     assert error.value.detail == "Could not find post with id 99."


# def test_if_status_code_is_equal_to_409_when_duplicate_post_is_sent() -> None:
#     post: list = []
#     with pytest.raises(HTTPException) as error:
#         check_if_post_is_duplicate(post=post)
#     assert error.value.status_code == status.HTTP_409_CONFLICT
