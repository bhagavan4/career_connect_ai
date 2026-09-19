from fastapi import APIRouter

from app.schemas.ai import CareerRecommendationRequest, CareerRecommendationResponse
from app.services.ai_service import generate_career_recommendation

router = APIRouter(prefix="/api/ai", tags=["AI"])

@router.post("/career-roadmap", response_model=CareerRecommendationResponse)
def career_roadmap(request: CareerRecommendationRequest):
    return generate_career_recommendation(
        company=request.company,
        role=request.role,
        skills=request.skills,
    )
