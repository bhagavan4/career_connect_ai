import json
import os

from openai import OpenAI


def generate_career_recommendation(company: str | None, role: str | None, skills: list[str]) -> dict:
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        return fallback_recommendation(company, role, skills)

    client = OpenAI(api_key=api_key)
    prompt = f"""
Create a concise career roadmap for:
Company: {company or "Not specified"}
Role: {role or "Software Engineer"}
Current skills: {", ".join(skills) or "Not specified"}

Return JSON with exactly these keys:
skills_to_learn, suggested_projects, interview_topics, roadmap.
Each value must be a short list of strings.
"""
    response = client.chat.completions.create(
        model=os.getenv("OPENAI_MODEL", "gpt-4o-mini"),
        messages=[
            {"role": "system", "content": "You are a practical career roadmap assistant."},
            {"role": "user", "content": prompt},
        ],
        response_format={"type": "json_object"},
        temperature=0.2,
    )
    return json.loads(response.choices[0].message.content)


def generate_networking_message(
    employee_name: str,
    company: str,
    role: str,
    university: str | None = None,
) -> str:
    api_key = os.getenv("OPENAI_API_KEY")
    if api_key:
        client = OpenAI(api_key=api_key)
        prompt = f"""
Write a short professional networking message to {employee_name}, who works as
a {role} at {company}. The sender is interested in the same career path.
University connection: {university or "not specified"}.
Ask politely for career guidance or advice, not a job guarantee or referral.
Keep it under 80 words.
"""
        response = client.chat.completions.create(
            model=os.getenv("OPENAI_MODEL", "gpt-4o-mini"),
            messages=[
                {"role": "system", "content": "Write concise, respectful professional networking messages."},
                {"role": "user", "content": prompt},
            ],
            temperature=0.4,
        )
        return response.choices[0].message.content.strip()

    university_line = (
        f" I noticed we share a connection with {university}."
        if university else ""
    )
    return (
        f"Hi {employee_name}, I’m exploring {role} opportunities at {company} "
        f"and would appreciate any advice on preparing for this career path."
        f"{university_line} Thanks for your time!"
    )


def fallback_recommendation(company: str | None, role: str | None, skills: list[str]) -> dict:
    role_text = (role or "").lower()
    if "backend" in role_text or "software" in role_text or not role:
        return {
            "skills_to_learn": ["Java", "Spring Boot", "SQL", "REST APIs", "DSA", "Microservices"],
            "suggested_projects": ["E-commerce REST API", "URL Shortener", "API Gateway Rate Limiter"],
            "interview_topics": ["Java/OOP", "DSA", "SQL", "Spring Boot", "System Design Basics"],
            "roadmap": ["Strengthen Java", "Build Spring Boot APIs", "Practice DSA and SQL", "Build one production-style backend project"],
        }

    return {
        "skills_to_learn": ["DSA", "OOP", "SQL", "REST APIs"],
        "suggested_projects": ["Role-specific CRUD API", "Authentication Service"],
        "interview_topics": ["DSA", "OOP", "SQL", "Project Discussion"],
        "roadmap": ["Learn core concepts", "Build a project", "Practice interview questions"],
    }
