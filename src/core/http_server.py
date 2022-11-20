from fastapi import FastAPI

from src.routes.posts_routes import posts_routes
from src.routes.root_routes import root_routes

app = FastAPI(
    title="Blog",
    description="CRUD for managing blog posts.",
    version="1.0.0",
    license_info={"name": "MIT"},
)

app.include_router(root_routes)
app.include_router(posts_routes)
