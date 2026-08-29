from fastapi import APIRouter
from pydantic import BaseModel

from app.services.ai_provider import generate_reply

router = APIRouter()


class ChatRequest(BaseModel):
    message: str


@router.post("/chat")
def chat(request: ChatRequest):

    message = request.message.strip()

    if not message:
        return {
            "status": "error",
            "error": "Message cannot be empty."
        }

    result = generate_reply(message)

    return {
        "status": "success",
        "mode": result.get("mode", "provider"),
        "message": message,
        "reply": result.get("reply", "")
    }