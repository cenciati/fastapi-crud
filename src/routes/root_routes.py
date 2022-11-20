from fastapi import APIRouter, status
from fastapi.responses import JSONResponse

root_routes = APIRouter()


@root_routes.get("/api/v1")
async def root() -> JSONResponse:
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content={
            "data": ["Welcome to my personal blog!"],
            "links": {"self": "/", "posts": "/posts"},
        },
    )
