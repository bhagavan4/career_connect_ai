# Career Connect AI Backend

FastAPI backend for an AI-powered career and alumni matchmaking platform.

## Run locally

From the repository root:

```bash
cd backend
python -m venv .venv
```

### Windows

```bash
.venv\Scripts\activate
```

### Install dependencies

```bash
pip install -r ../requirements.txt
```

### Start server

```bash
uvicorn app.main:app --reload
```

The API will be available at:

- `http://127.0.0.1:8000`
- Swagger UI: `http://127.0.0.1:8000/docs`

## Current endpoints

- `GET /`
- `GET /api/health`
- `POST /api/career/analyze`

The current implementation is intentionally small. AI query extraction, PostgreSQL persistence, employee/alumni matching, and personalized career roadmaps will be added incrementally.
