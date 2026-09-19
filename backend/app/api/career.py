from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.database import get_db
from app.schemas.career import CareerQueryRequest, CareerQueryResponse, CareerTarget
from app.services.career_service import analyze_career_query

router = APIRouter(prefix="/api/career", tags=["Career"])


@router.post("/analyze", response_model=dict)
def analyze(request: CareerQueryRequest, db: Session = Depends(get_db)):
    return analyze_career_query(db=db, query=request.query)
