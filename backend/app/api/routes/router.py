from fastapi import APIRouter

from app.api.routes.research import router as research_router
from app.api.routes.sources import router as sources_router
from app.api.routes.findings import router as findings_router
from app.api.routes.chat import router as chat_router

api_router = APIRouter()

api_router.include_router(
    research_router,
    tags=["Research"]
)

api_router.include_router(
    sources_router,
    tags=["Sources"]
)

api_router.include_router(
    findings_router,
    tags=["Findings"]
)

api_router.include_router(
    chat_router,
    tags=["Chat"]
)