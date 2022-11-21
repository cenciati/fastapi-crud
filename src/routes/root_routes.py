from fastapi import APIRouter, status

root_routes = APIRouter()


@root_routes.get(
    "/api/v1", status_code=status.HTTP_200_OK, response_model=dict
)
async def root() -> dict:
    return {
        "data": ["Welcome to my personal blog!"],
        "links": {"self": "/", "posts": "/posts"},
    }
