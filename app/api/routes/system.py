from fastapi import APIRouter

router = APIRouter(prefix="/api/system", tags=["System"])


@router.get("/status")
def system_status():
    return {
        "status": "online",
        "service": "EMERGENT",
        "message": "System API is working."
    }