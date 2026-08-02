from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.database import get_db
from app.database.models import Finding

router = APIRouter()


@router.get("/findings")
def get_findings(
    db: Session = Depends(get_db)
):

    return db.query(Finding).all()