from db.database import BaseModel, engine
from fastapi import FastAPI
from routes import emotion, background_task, websocket
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
### missing firebase config and service account key
# app.include_router(auth.router)
app.include_router(background_task.router)
app.include_router(websocket.router)

BaseModel.metadata.create_all(engine)
