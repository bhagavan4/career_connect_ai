import re

COMPANIES = [
    "Swiggy",
    "Amazon",
    "Microsoft",
    "Google",
    "Flipkart",
    "Infosys",
    "TCS",
    "Wipro",
]


def extract_company(query: str) -> str | None:
    query_lower = query.lower()

    for company in COMPANIES:
        if company.lower() in query_lower:
            return company

    return None


def extract_role(query: str) -> str | None:
    query_lower = query.lower()

    role_patterns = {
        "Software Engineer": r"\b(sde|software engineer|software developer)\b",
        "Backend Developer": r"\b(backend developer|backend engineer)\b",
        "Frontend Developer": r"\b(frontend developer|frontend engineer)\b",
        "Data Scientist": r"\b(data scientist)\b",
        "Data Analyst": r"\b(data analyst)\b",
        "DevOps Engineer": r"\b(devops engineer|devops)\b",
    }

    for role, pattern in role_patterns.items():
        if re.search(pattern, query_lower):
            return role

    return None


def parse_career_query(query: str) -> dict:
    return {
        "company": extract_company(query),
        "role": extract_role(query),
        "intent": "career_guidance",
    }
