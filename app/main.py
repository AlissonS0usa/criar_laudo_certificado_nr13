from fastapi import FastAPI
from app.models import base  # isso garante que os modelos sejam importados
from app.routers import auth

app = FastAPI()

app.include_router(auth.router)


