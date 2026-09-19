from fastapi import APIRouter, Depends
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.db.database import get_db
from app.db.models import Employee

router = APIRouter(prefix="/api/employees", tags=["Employees"])


@router.get("")
def list_employees(db: Session = Depends(get_db)):
    employees = db.scalars(select(Employee)).all()

    return [
        {
            "id": employee.id,
            "name": employee.name,
            "company": employee.company,
            "role": employee.role,
            "university": employee.university,
            "experience_years": employee.experience_years,
            "skills": employee.skills,
        }
        for employee in employees
    ]
