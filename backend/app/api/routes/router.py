from fastapi import APIRouter

from app.api.routes.research import router as research_router
from app.api.routes.sources import router as sources_router

api_router = APIRouter()

api_router.include_router(
    research_router,
    tags=["Research"]
)

api_router.include_router(
    sources_router,
    tags=["Sources"]
)