from src.core.schemas import BaseModel


class ChatResponse(BaseModel):
    sender: str = "your"
    message: str
    type: str
