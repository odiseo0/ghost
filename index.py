from fastapi import FastAPI, Request, WebSocket, WebSocketDisconnect
from fastapi.responses import ORJSONResponse
from fastapi.templating import Jinja2Templates

from src.core.chains.chat import chat_chain
from src.api.chats.domain import ChatResponse


app = FastAPI(default_response_class=ORJSONResponse)
templates = Jinja2Templates(directory="html")


@app.get("/")
async def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.websocket("/chat")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()

    while True:
        try:
            question = await websocket.receive_text()
            q_resp = ChatResponse(sender="you", message=question, type="stream")
            await websocket.send_json(q_resp.dict(by_alias=True))

            response = await chat_chain.arun(question)

            ai_resp = ChatResponse(sender="bot", message=response, type="start")
            await websocket.send_json(ai_resp.dict(by_alias=True))

            end_resp = ChatResponse(sender="bot", message=response, type="end")
            await websocket.send_json(end_resp.dict(by_alias=True))
        except WebSocketDisconnect:
            break
        except Exception:
            resp = ChatResponse(
                sender="bot",
                message="Sorry, something went wrong. Try again.",
                type="error",
            )
            await websocket.send_json(resp.dict())
