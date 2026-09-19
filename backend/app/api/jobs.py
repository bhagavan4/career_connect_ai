from fastapi import APIRouter, Depends
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.db.database import get_db
from app.db.models import Job

router = APIRouter(prefix="/api/jobs", tags=["Jobs"])


@router.get("")
def list_jobs(db: Session = Depends(get_db)):
    jobs = db.scalars(select(Job)).all()

    return [
        {
            "id": job.id,
            "company": job.company,
            "title": job.title,
            "location": job.location,
            "experience_level": job.experience_level,
            "required_skills": job.required_skills,
        }
        for job in jobs
    ]
