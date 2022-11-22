from fastapi import APIRouter, status

root_router = APIRouter()


@root_router.get("/", status_code=status.HTTP_200_OK, response_model=dict)
async def root() -> dict:
    return {
        "data": ["Welcome to my personal blog!"],
        "links": {"self": "/", "posts": "/posts"},
    }
