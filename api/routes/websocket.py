from fastapi import WebSocket, APIRouter, WebSocketDisconnect
from datetime import datetime
import time

router = APIRouter(prefix="/websocket", tags=["websocket"])

@router.websocket("/send-receive-messages-to-server")
async def websocket_basic(websocket: WebSocket):
    await websocket.accept()

    while True:
        data = await websocket.receive_text()

        # long running task
        time.sleep(1)

        await websocket.send_text(f"Message text was: {data}")

@router.websocket("/receive-notifs-hardcoded")
async def websocket_receive_notifs_hardcoded(websocket: WebSocket):
    await websocket.accept()

    notif_queue = [
        "Maybe make a new account? 🤔",
        "Your account has been hacked 😔",
        "Your character just reached level 3 🥳",
        "Your character just reached level 2 🥳",
        "Your account has been successfully created 🥳",
        ]

    while True:
        await websocket.send_text(f"New notif: {notif_queue.pop()}")

        # await for new notifs
        time.sleep(2)


class ConnectionManager:
    def __init__(self):
        self.active_connections: list[WebSocket] = []

    async def connect(self, websocket: WebSocket):
        await websocket.accept()
        self.active_connections.append(websocket)

    def disconnect(self, websocket: WebSocket):
        self.active_connections.remove(websocket)

    async def send_personal_message(self, message: str, websocket: WebSocket):
        await websocket.send_text(message)

    async def broadcast(self, message: str):
        for connection in self.active_connections:
            await connection.send_text(message)


manager = ConnectionManager()



@router.websocket("/notifs/")
async def websocket_endpoint(websocket: WebSocket):
    await manager.connect(websocket)
    await manager.broadcast(f"A new user joined the chat")
    try:
        while True:
            data = await websocket.receive_json()
            # await manager.send_personal_message(f"You wrote: {data['message']}", websocket)
            await manager.broadcast(f"{data['username']} says: {data['message']}")
    except WebSocketDisconnect:
        manager.disconnect(websocket)
        await manager.broadcast(f"{data['username']} left the chat")