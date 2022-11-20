from os import getenv
from typing import Optional

from dotenv import find_dotenv, load_dotenv
from fastapi import APIRouter, HTTPException, status
from fastapi.responses import JSONResponse

from src.infra.database import create_database_connection
from src.models.post import Post

load_dotenv(find_dotenv())
DB_HOST: str = getenv("DB_HOST")
DB_DATABASE: str = getenv("DB_DATABASE")
DB_USER: str = getenv("DB_USER")
DB_PASSWORD: str = getenv("DB_PASSWORD")

posts_routes = APIRouter()
connection, cursor = create_database_connection(
    host=DB_HOST,
    database=DB_DATABASE,
    user=DB_USER,
    password=DB_PASSWORD,
)


def check_if_post_exists(
    id: Optional[int] = None, post: Optional[Post] = None
) -> None:
    if id and not post:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Could not find post with id {id}.",
        )

    if not id and not post:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Could not find any post.",
        )

    return None


@posts_routes.get("/api/v1/posts")
async def get_all_posts() -> JSONResponse:
    cursor.execute("SELECT * FROM posts")
    posts = cursor.fetchall()
    check_if_post_exists(post=posts)

    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content={
            "data": posts,
            "links": {"self": "/posts", "root": "/"},
        },
    )


@posts_routes.get("/api/v1/posts/{id}")
async def get_one_post(id: int) -> JSONResponse:
    cursor.execute(f"SELECT * FROM posts WHERE id = {id}")
    post = cursor.fetchone()
    check_if_post_exists(id=id, post=post)

    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content={
            "data": [post],
            "links": {"self": f"/posts/{id}", "root": "/"},
        },
    )


@posts_routes.post("/api/v1/posts")
async def create_post(post: Post) -> JSONResponse:
    cursor.execute(
        """
        INSERT INTO
        posts (id, author, title, content)
        VALUES (%s, %s, %s, %s)
        RETURNING *
        """,
        (post.id, post.author, post.title, post.content),
    )
    post = cursor.fetchone()
    connection.commit()

    return JSONResponse(
        status_code=status.HTTP_201_CREATED,
        content={
            "data": [post],
            "links": {"self": "/posts", "root": "/"},
        },
    )


@posts_routes.delete("/api/v1/posts/{id}")
async def delete_post(id: int) -> JSONResponse:
    cursor.execute(f"DELETE FROM posts WHERE id = {id} RETURNING *")
    post = cursor.fetchone()
    check_if_post_exists(id=id, post=post)
    connection.commit()

    return JSONResponse(status_code=status.HTTP_204_NO_CONTENT, content=None)


@posts_routes.put("/api/v1/posts/{id}")
async def update_post(id: int, post: Post) -> JSONResponse:
    cursor.execute(
        """
        UPDATE posts SET
        author = %s,
        title = %s,
        content = %s
        WHERE id = %s
        RETURNING *
        """,
        (post.author, post.title, post.content, id),
    )
    post = cursor.fetchone()
    check_if_post_exists(id=id, post=post)
    connection.commit()

    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content={
            "data": [post],
            "links": {"self": f"/posts/{id}", "root": "/"},
        },
    )


"""
GET 200
/posts?limit=10

GET 200
serach by keyword
/posts?contains=mlops
"""
