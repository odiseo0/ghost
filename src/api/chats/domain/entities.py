from src.core.schemas import BaseModel


class ChatResponse(BaseModel):
    sender: str = "you"
    message: str
    type: str
