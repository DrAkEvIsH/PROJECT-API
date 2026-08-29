from fastapi import APIRouter

router = APIRouter(tags=["System"])


@router.get("/status")
def system_status():
    return {
        "status": "online",
        "service": "EMERGENT",
        "message": "System API is working."
    }
