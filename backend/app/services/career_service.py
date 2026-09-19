from sqlalchemy.orm import Session

from app.services.matching_service import find_matching_employees
from app.services.query_parser import parse_career_query


def analyze_career_query(db: Session, query: str) -> dict:
    parsed = parse_career_query(query)

    matches = find_matching_employees(
        db=db,
        company=parsed["company"],
        role=parsed["role"],
        skills=[],
        limit=5,
    )

    return {
        "query": query,
        "target": {
            "company": parsed["company"],
            "role": parsed["role"],
        },
        "intent": parsed["intent"],
        "matches": matches,
    }
