from db.database import BaseModel, engine
from fastapi import FastAPI
from routes import emotion


app = FastAPI()

app.include_router(emotion.router)

BaseModel.metadata.create_all(engine)
