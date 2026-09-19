from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.ai import router as ai_router
from app.api.career import router as career_router
from app.api.employees import router as employees_router
from app.api.jobs import router as jobs_router
from app.api.matching import router as matching_router

app = FastAPI(
    title="Career Connect AI",
    description="AI-powered career and alumni matchmaking backend",
    version="0.1.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "https://career-connect-ai-blue.vercel.app",
        "http://localhost:3000",
        "http://127.0.0.1:3000",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(career_router)
app.include_router(employees_router)
app.include_router(jobs_router)
app.include_router(matching_router)
app.include_router(ai_router)


@app.get("/api/health")
def health_check():
    return {
        "status": "healthy",
        "service": "career-connect-ai",
    }


@app.get("/")
def root():
    return {
        "message": "Career Connect AI backend is running"
    }
