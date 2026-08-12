from fastapi import FastAPI
from app.database.database import Base, engine
from app.core.config import settings
from app.core.logging import setup_logging
from app.database import models
from app.api.routes.router import api_router
from fastapi.middleware.cors import CORSMiddleware


logger = setup_logging()

app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION,
    description="Enterprise AI Research Platform"
)

from fastapi.middleware.cors import CORSMiddleware

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

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Register all API routes
app.include_router(api_router)


@app.on_event("startup")
def startup():
    Base.metadata.create_all(bind=engine)

    logger.info("Database initialized")
    
    logger.info("Application started successfully")


@app.get("/")
def root():
    return {
        "application": settings.APP_NAME,
        "version": settings.APP_VERSION,
        "status": "running"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }