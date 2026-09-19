from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from app.core.config import settings
from app.db.database import Base
from app.db.models import Employee, Job, University


def seed_database():
    engine = create_engine(settings.database_url, pool_pre_ping=True)
    Base.metadata.create_all(bind=engine)

    with Session(engine) as db:
        if db.query(Employee).first():
            print("Database already contains employee data. Skipping seed.")
            return

        universities = [
            University(name="Indian Institute of Technology Hyderabad", location="Hyderabad"),
            University(name="Indian Institute of Technology Tirupati", location="Tirupati"),
        ]

        db.add_all(universities)
        db.flush()

        employees = [
            Employee(
                name="Arjun Rao",
                company="Swiggy",
                role="Software Engineer",
                university="Indian Institute of Technology Hyderabad",
                experience_years=2,
                skills="Java, Spring Boot, PostgreSQL, Redis, REST APIs",
            ),
            Employee(
                name="Priya Sharma",
                company="Swiggy",
                role="Backend Engineer",
                university="Indian Institute of Technology Tirupati",
                experience_years=3,
                skills="Java, Spring Boot, Microservices, AWS, PostgreSQL",
            ),
            Employee(
                name="Rahul Verma",
                company="Amazon",
                role="Software Engineer",
                university="Indian Institute of Technology Hyderabad",
                experience_years=4,
                skills="Java, Python, AWS, Data Structures, System Design",
            ),
        ]

        jobs = [
            Job(
                company="Swiggy",
                title="Software Development Engineer",
                location="Bengaluru",
                experience_level="Entry Level",
                required_skills="Java, DSA, Spring Boot, SQL, REST APIs",
            ),
            Job(
                company="Amazon",
                title="Software Development Engineer I",
                location="Bengaluru",
                experience_level="Entry Level",
                required_skills="Java, DSA, OOP, SQL, System Design",
            ),
        ]

        db.add_all(employees)
        db.add_all(jobs)
        db.commit()

        print("Sample career data inserted successfully.")


if __name__ == "__main__":
    seed_database()
