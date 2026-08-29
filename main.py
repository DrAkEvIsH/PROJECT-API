from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

from app.core.config import settings
from app.api.routes.system import router as system_router
from app.api.routes.ai.chat import router as ai_router


app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {
        "status": "online",
        "project": settings.APP_NAME,
        "version": settings.APP_VERSION,
        "message": "Backend is working."
    }

@app.get("/health")
def health():
    return {
        "status": "ok",
        "project": settings.APP_NAME,
        "version": settings.APP_VERSION
    }

@app.get("/health")
def health():
    return {
        "status": "healthy"
    }


app.include_router(system_router)
app.include_router(ai_router)
app.mount("/app", StaticFiles(directory="frontend", html=True), name="frontend")