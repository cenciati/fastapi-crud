from pydantic import BaseSettings


class Settings(BaseSettings):
    API_V1_STR: str = "/api/v1"
    URL: str = f"http://localhost:8000{API_V1_STR}"


settings = Settings()
