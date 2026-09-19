from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.database import get_db
from app.schemas.matching import EmployeeMatchRequest, EmployeeMatchResponse
from app.services.matching_service import find_matching_employees

router = APIRouter(prefix="/api/matching", tags=["Matching"])


@router.post("/employees", response_model=EmployeeMatchResponse)
def match_employees(
    request: EmployeeMatchRequest,
    db: Session = Depends(get_db),
):
    matches = find_matching_employees(
        db=db,
        company=request.company,
        role=request.role,
        skills=request.skills,
        limit=request.limit,
    )

    return EmployeeMatchResponse(matches=matches)
