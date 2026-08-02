from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.database import get_db
from app.schemas.research import (
    ResearchRequest,
    ResearchResponse,
)
from app.services.research_service import create_research_session

router = APIRouter()


@router.post(
    "/research",
    response_model=ResearchResponse,
)
def create_research(
    request: ResearchRequest,
    db: Session = Depends(get_db),
):
    session = create_research_session(
        db,
        request.topic,
    )

    return session