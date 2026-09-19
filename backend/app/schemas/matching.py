from pydantic import BaseModel, Field


class EmployeeMatchRequest(BaseModel):
    company: str | None = None
    role: str | None = None
    skills: list[str] = Field(default_factory=list)
    limit: int = Field(default=5, ge=1, le=20)


class EmployeeMatchResponse(BaseModel):
    matches: list[dict]
