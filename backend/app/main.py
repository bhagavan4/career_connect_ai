from fastapi import FastAPI

app = FastAPI(
    title="Career Connect AI",
    description="AI-powered career and alumni matchmaking backend",
    version="0.1.0",
)


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
