from sqlalchemy import select
from sqlalchemy.orm import Session

from app.db.models import Employee


def _normalize(value: str | None) -> str:
    return (value or "").strip().lower()


def _skill_set(value: str | None) -> set[str]:
    return {
        skill.strip().lower()
        for skill in (value or "").split(",")
        if skill.strip()
    }


def find_matching_employees(
    db: Session,
    company: str | None,
    role: str | None,
    skills: list[str] | None = None,
    limit: int = 5,
) -> list[dict]:
    requested_skills = {skill.strip().lower() for skill in (skills or []) if skill.strip()}

    query = select(Employee)
    if company:
        query = query.where(Employee.company.ilike(f"%{company}%"))

    employees = db.scalars(query).all()
    matches = []

    for employee in employees:
        score = 0

        if company and _normalize(employee.company) == _normalize(company):
            score += 50

        if role and _normalize(employee.role) == _normalize(role):
            score += 30

        matching_skills = _skill_set(employee.skills).intersection(requested_skills)
        score += min(len(matching_skills) * 5, 20)

        if score > 0:
            matches.append({
                "id": employee.id,
                "name": employee.name,
                "company": employee.company,
                "role": employee.role,
                "university": employee.university,
                "experience_years": employee.experience_years,
                "skills": employee.skills,
                "match_score": score,
            })

    matches.sort(key=lambda item: item["match_score"], reverse=True)
    return matches[:limit]
