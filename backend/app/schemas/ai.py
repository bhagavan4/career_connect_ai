from pydantic import BaseModel, Field

class CareerRecommendationRequest(BaseModel):
    company: str | None = None
    role: str | None = None
    skills: list[str] = Field(default_factory=list)

class CareerRecommendationResponse(BaseModel):
    skills_to_learn: list[str]
    suggested_projects: list[str]
    interview_topics: list[str]
    roadmap: list[str]
