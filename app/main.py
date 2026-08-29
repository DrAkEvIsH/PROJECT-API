from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.routes import system
from app.api.routes.ai import chat

app = FastAPI(
    title="PROJECT API",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(system.router, prefix="/api/system")

app.include_router(chat.router, prefix="/api/ai")


@app.get("/")
def root():
    return {
        "status": "SUCCESS",
        "name": "PROJECT API",
        "version": "1.0.0"
    }