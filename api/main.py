import os
import uvicorn

from db.database import BaseModel, engine
from fastapi import FastAPI
from routes import emotion, background_task, websocket, auth, user
from fastapi.staticfiles import StaticFiles

from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

# TODO: limit permissions
allow_all = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=allow_all,
    allow_credentials=True,
    allow_methods=allow_all,
    allow_headers=allow_all,
)

app.mount("/static", StaticFiles(directory="static"), name="static")

app.include_router(emotion.router)
app.include_router(auth.router)
app.include_router(user.router)
app.include_router(background_task.router)
app.include_router(websocket.router)

BaseModel.metadata.create_all(engine)

if __name__ == "__main__":
    uvicorn.run(app, port=int(os.environ.get("PORT", 8000)), host="0.0.0.0")
