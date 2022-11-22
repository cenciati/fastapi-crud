from fastapi import FastAPI

from src.core.config import settings
from src.routes.posts_routes import posts_router
from src.routes.root_routes import root_router

app = FastAPI(
    title="Blog",
    description="CRUD for managing blog posts.",
    version="1.0.0",
    license_info={"name": "MIT"},
)

app.include_router(root_router)
app.include_router(posts_router, prefix=settings.API_V1_STR)
