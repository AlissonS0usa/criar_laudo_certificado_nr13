from fastapi import FastAPI
from app.models import base  # isso garante que os modelos sejam importados

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "API rodando com PostgreSQL"}
