"""Chat endpoint."""

from openai import APIError

from fastapi import APIRouter, HTTPException

from app.schemas.chat import ChatRequest, ChatResponse
from app.services.openai_service import get_travel_itinerary

router = APIRouter()


@router.post("", response_model=ChatResponse)
async def chat(request: ChatRequest) -> ChatResponse:
    """
    Accept a user message, send it to the LLM, and return the AI-generated travel itinerary.
    """
    try:
        response_text = await get_travel_itinerary(request.message)
        return ChatResponse(response=response_text)
    except ValueError as e:
        if "OPENAI_API_KEY" in str(e):
            raise HTTPException(status_code=503, detail="OpenAI API is not configured") from e
        raise HTTPException(status_code=400, detail=str(e)) from e
    except APIError as e:
        raise HTTPException(status_code=502, detail="OpenAI API request failed") from e
