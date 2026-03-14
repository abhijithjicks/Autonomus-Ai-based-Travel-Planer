"""OpenAI integration for generating travel itineraries."""

from openai import AsyncOpenAI

from app.core.config import settings

SYSTEM_PROMPT = """You are a helpful travel planner. Given the user's request, respond with a clear, practical travel itinerary. Include suggestions for activities, timing, and practical tips when relevant. Keep the response focused and easy to read."""


async def get_travel_itinerary(user_message: str) -> str:
    """
    Send the user message to the LLM and return the generated travel itinerary.
    """
    if not settings.openai_api_key:
        raise ValueError("OPENAI_API_KEY is not set in environment")

    client = AsyncOpenAI(api_key=settings.openai_api_key)

    response = await client.chat.completions.create(
        model=settings.openai_model,
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": user_message},
        ],
    )

    content = response.choices[0].message.content
    return content.strip() if content else ""
