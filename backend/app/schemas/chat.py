"""Chat API schemas."""

from pydantic import BaseModel, Field


class ChatRequest(BaseModel):
    """Incoming chat message."""

    message: str = Field(..., min_length=1, description="User message for travel planning")


class ChatResponse(BaseModel):
    """Chat API response."""

    response: str = Field(..., description="Travel planning response text")
