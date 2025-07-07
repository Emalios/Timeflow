from fastapi import FastAPI, APIRouter
from api import api_router

app = FastAPI(title="Timelapse Backend")

app.include_router(api_router, prefix="/api")

@app.get("/")
async def root():
    return {"message": "Hello World"}