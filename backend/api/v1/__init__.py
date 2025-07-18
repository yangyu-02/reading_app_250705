from fastapi import APIRouter

api_router = APIRouter()


@api_router.get("/health")
async def health_check() -> dict:
    return {"status": "healthy"}
