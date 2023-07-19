from fastapi import WebSocket, APIRouter
from datetime import datetime
import time

router = APIRouter(prefix="/websocket", tags=["websocket"])

@router.websocket("/send-receive-messages-to-server")
async def websocket_endpoint_basic(websocket: WebSocket):
    await websocket.accept()

    while True:
        data = await websocket.receive_text()

        # long running task
        time.sleep(1)

        await websocket.send_text(f"Message text was: {data}")

@router.websocket("/receive-notifs")
async def websocket_endpoint_basic(websocket: WebSocket):
    await websocket.accept()

    notif_queue = [
        "Maybe make a new account? 🤔",
        "Your account has been hacked 😔",
        "Your character just reached level 3 🥳",
        "Your character just reached level 2 🥳",
        "You account has been successfully created 🥳",
        ]

    while True:
        if notif_queue:
            await websocket.send_text(f"New notif: {notif_queue.pop()}")

        # await for new notifs
        time.sleep(2)
