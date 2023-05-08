from litestar import WebSocket
from litestar.handlers import websocket_listener

from src.core.chains.chat import chat_chain
from ..domain import ChatResponse


@websocket_listener("/chat")
async def general_chat(data: str, socket: WebSocket) -> None:
    q_resp = ChatResponse(sender="you", message=data, type="stream")
    await socket.send_json(q_resp.dict())

    response = await chat_chain.arun(data)

    ai_resp = ChatResponse(sender="bot", message=response, type="start")
    await socket.send_json(ai_resp.dict())

    end_resp = ChatResponse(sender="bot", message=response, type="end")
    await socket.send_json(end_resp.dict())
