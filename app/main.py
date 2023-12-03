from fastapi import FastAPI
from .routers import goals

app = FastAPI(title="Goal API", version="0.0.1")

app.include_router(goals.router)

@app.get("/")
async def root():
    return {"message": "Hello Students!"}

lista1 =list()