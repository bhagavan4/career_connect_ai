from pydantic import BaseModel, Field


class CareerQueryRequest(BaseModel):
    query: str = Field(..., min_length=3, description="User's career question")


class CareerTarget(BaseModel):
    company: str | None = None
    role: str | None = None


class CareerQueryResponse(BaseModel):
    query: str
    target: CareerTarget
    intent: str
