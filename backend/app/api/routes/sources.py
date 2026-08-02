from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.database import get_db
from app.database.models import Source

router = APIRouter()


@router.get("/sources")
def get_sources(
    db: Session = Depends(get_db)
):

    return db.query(Source).all()