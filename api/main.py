from db.database import BaseModel, engine
from fastapi import FastAPI
from routes import emotion
from routes import auth

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

app.include_router(emotion.router)
app.include_router(auth.router)

BaseModel.metadata.create_all(engine)
