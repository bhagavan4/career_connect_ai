from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter(prefix="/api/career", tags=["Career"])


class CareerQuery(BaseModel):
    query: str


@router.post("/analyze")
def analyze_career_query(request: CareerQuery):
    # Basic MVP response. AI query extraction will be added next.
    return {
        "query": request.query,
        "message": "Career query received successfully",
    }
