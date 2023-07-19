from fastapi import WebSocket, APIRouter
from datetime import datetime
import time

router = APIRouter(prefix="/websocket", tags=["websocket"])

@router.websocket("/send-receive-messages-to-server")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()

    while True:
        data = await websocket.receive_text()

        # long running task
        time.sleep(1)

        await websocket.send_text(f"Message text was: {data}")
