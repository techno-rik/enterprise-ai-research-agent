from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.database.database import Base, engine
from app.core.config import settings
from app.core.logging import setup_logging
from app.database import models
from app.api.routes.router import api_router


logger = setup_logging()


app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION,
    description="Enterprise AI Research Platform"
)


# ============================================================
# CORS CONFIGURATION
# ============================================================

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "https://enterprise-ai-research-agent.vercel.app",
        "https://enterprise-ai-research-agent-git-main-acme-ea95.vercel.app",
        "https://enterprise-ai-research-agent-cnmwbcdau-acme-ea95.vercel.app",
        "http://localhost:5173",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# ============================================================
# REGISTER API ROUTES
# ============================================================

app.include_router(api_router)


# ============================================================
# STARTUP
# ============================================================

@app.on_event("startup")
def startup():
    Base.metadata.create_all(bind=engine)

    logger.info("Database initialized")
    logger.info("Application started successfully")


# ============================================================
# ROOT ENDPOINT
# ============================================================

@app.get("/")
def root():
    return {
        "application": settings.APP_NAME,
        "version": settings.APP_VERSION,
        "status": "running"
    }


# ============================================================
# HEALTH CHECK
# ============================================================

@app.get("/health")
def health():
    return {
        "status": "healthy"
    }