from fastapi import APIRouter

from app.schemas.career import CareerQueryRequest, CareerQueryResponse, CareerTarget
from app.services.query_parser import parse_career_query

router = APIRouter(prefix="/api/career", tags=["Career"])


@router.post("/analyze", response_model=CareerQueryResponse)
def analyze_career_query(request: CareerQueryRequest):
    parsed = parse_career_query(request.query)

    return CareerQueryResponse(
        query=request.query,
        target=CareerTarget(
            company=parsed["company"],
            role=parsed["role"],
        ),
        intent=parsed["intent"],
    )
