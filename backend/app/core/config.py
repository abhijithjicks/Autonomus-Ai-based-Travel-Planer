"""Application settings."""

from typing import List

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """App configuration loaded from environment."""

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
    )

    app_name: str = "AI Travel API"
    debug: bool = False
    cors_origins: List[str] = ["http://localhost:5173"]
    openai_api_key: str = ""
    openai_model: str = "gpt-4o-mini"


settings = Settings()
