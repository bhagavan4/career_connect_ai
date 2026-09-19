# Career Connect AI - Backend Design & Structure

## 1. Backend Goal

The backend powers an AI career and alumni matchmaking assistant.

Example user query:

> How can I crack an SDE role at Swiggy?

The backend should:
1. Understand the user's career query.
2. Extract company, role, skills, university, and other useful context.
3. Search the internal employee/alumni/job database.
4. Match relevant employees or alumni.
5. Generate a company/role-specific preparation roadmap.
6. Generate a personalized networking/referral message.
7. Return a structured response to the frontend.

---

## 2. Initial Technology Stack

- Python 3.11+
- FastAPI
- Uvicorn
- PostgreSQL
- SQLAlchemy
- Pydantic
- OpenAI API
- HTTPX
- python-dotenv

---

## 3. Backend Architecture

```
Frontend (React)
       |
       | HTTP / REST API
       v
+-------------------------+
|      FastAPI App        |
+-------------------------+
       |
       +--------------------+
       |                    |
       v                    v
 Query / AI Service    Matching Service
       |                    |
       v                    v
    OpenAI API         PostgreSQL
       |                    |
       +---------+----------+
                 |
                 v
          Structured Response
                 |
                 v
            React Frontend
```

---

## 4. Recommended Project Structure

```
backend/
├── app/
│   ├── __init__.py
│   ├── main.py
│   │
│   ├── api/
│   │   ├── __init__.py
│   │   ├── career.py
│   │   ├── employees.py
│   │   ├── jobs.py
│   │   └── health.py
│   │
│   ├── core/
│   │   ├── __init__.py
│   │   ├── config.py
│   │   └── security.py
│   │
│   ├── db/
│   │   ├── __init__.py
│   │   ├── database.py
│   │   └── models.py
│   │
│   ├── schemas/
│   │   ├── __init__.py
│   │   ├── career.py
│   │   ├── employee.py
│   │   └── job.py
│   │
│   ├── services/
│   │   ├── __init__.py
│   │   ├── ai_service.py
│   │   ├── employee_matching.py
│   │   ├── career_roadmap.py
│   │   └── networking_message.py
│   │
│   ├── repositories/
│   │   ├── __init__.py
│   │   ├── employee_repository.py
│   │   ├── job_repository.py
│   │   └── university_repository.py
│   │
│   └── utils/
│       ├── __init__.py
│       └── text_utils.py
│
├── tests/
│   ├── __init__.py
│   ├── test_health.py
│   ├── test_career.py
│   └── test_matching.py
│
├── .env.example
├── requirements.txt
└── README.md
```

---

## 5. Layer Responsibilities

### API Layer

Receives HTTP requests from React and returns JSON responses.

Example:

```
POST /api/career/analyze
POST /api/career/match
POST /api/career/message
GET  /api/employees
GET  /api/jobs
GET  /api/health
```

### Service Layer

Contains application/business logic.

- `ai_service.py` - communicates with the LLM.
- `employee_matching.py` - finds relevant employees/alumni.
- `career_roadmap.py` - creates preparation plans.
- `networking_message.py` - creates personalized messages.

### Repository Layer

Handles database access.

Repositories keep SQL/database logic separate from business logic.

### Database Layer

Stores:

- Users
- Employees
- Alumni
- Universities
- Companies
- Jobs
- Skills
- Career profiles

---

## 6. Main Database Entities

### User

```
id
name
email
university_id
skills
experience_level
target_role
target_company
```

### Employee

```
id
name
company
role
university_id
experience_years
skills
location
profile_url
is_alumni
```

### Job

```
id
company
title
location
experience_level
required_skills
description
```

### University

```
id
name
location
```

---

## 7. Career Query Flow

Example:

```
User:
"How do I crack an SDE role at Swiggy?"
              |
              v
        FastAPI endpoint
              |
              v
        AI Query Parser
              |
              v
{
  "company": "Swiggy",
  "role": "SDE"
}
              |
              v
       Database Search
              |
              v
 Matching Employees / Alumni
              |
              v
    Career Roadmap Generator
              |
              v
 Personalized Response
```

---

## 8. Matching Logic - MVP

Start with PostgreSQL filtering before adding vector search.

Possible matching factors:

1. Same company
2. Same target role
3. Same university
4. Similar skills
5. Similar experience
6. Similar career path

Example scoring concept:

```
company match       -> +40
role match          -> +25
university match    -> +20
skill similarity    -> +10
experience similarity -> +5
```

The score is only an internal matching mechanism, not a user-facing ranking of people.

Later, semantic embeddings/vector search can improve skill and career-path matching.

---

## 9. AI Service Responsibilities

The AI service should handle:

### Query Understanding

Convert:

```
"How can I get an SDE job at Swiggy?"
```

into structured information:

```json
{
  "company": "Swiggy",
  "role": "SDE",
  "intent": "career_guidance"
}
```

### Roadmap Generation

Generate:

- Required skills
- DSA topics
- Backend/system-design topics
- Relevant projects
- Interview preparation
- Suggested learning sequence

### Message Generation

Generate a short personalized message based on the matched employee/alumni profile.

---

## 10. API Response Design

Example:

```json
{
  "query": "How can I crack an SDE role at Swiggy?",
  "target": {
    "company": "Swiggy",
    "role": "SDE"
  },
  "roadmap": {
    "skills": [],
    "projects": [],
    "interview_preparation": []
  },
  "matches": [],
  "networking_message": ""
}
```

---

## 11. Environment Variables

Use `.env` locally and never commit secrets.

Example `.env.example`:

```
OPENAI_API_KEY=
DATABASE_URL=postgresql://username:password@localhost:5432/career_connect
```

---

## 12. Development Order

Build the backend in this order:

### Phase 1 - Foundation
- FastAPI application
- Health endpoint
- Configuration
- PostgreSQL connection

### Phase 2 - Database
- SQLAlchemy models
- Employee table
- University table
- Job table
- Seed sample data

### Phase 3 - Career API
- Career query endpoint
- Query parsing
- Company/role extraction

### Phase 4 - Matching
- Employee matching
- Alumni matching
- Skill matching

### Phase 5 - AI
- LLM integration
- Career roadmap generation
- Networking message generation

### Phase 6 - Frontend Integration
- React API client
- Career dashboard
- Matched alumni display
- Roadmap display
- Networking message UI

### Phase 7 - Advanced Search
- Embeddings
- Vector database
- Semantic profile matching

---

## 13. Important MVP Rule

Do not depend on scraping LinkedIn profiles.

For the first version, use:
- User-provided profiles
- Authorized data sources
- A prepared/sample employee and alumni dataset

This keeps the MVP simpler and avoids making the system dependent on an external platform's scraping restrictions.

---

## 14. Target Backend Flow

```
React
  |
  v
POST /api/career/analyze
  |
  v
Career Controller
  |
  +----> AI Service
  |          |
  |          +----> Query extraction
  |          +----> Roadmap generation
  |
  +----> Matching Service
             |
             +----> Employee Repository
             +----> Job Repository
             +----> University Repository
                         |
                         v
                    PostgreSQL
                         |
                         v
                 Structured Response
                         |
                         v
                       React
```

This structure is designed so that the MVP can be built simply first and expanded later without rewriting the entire backend.
