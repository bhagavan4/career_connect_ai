from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from app.db.database import Base


class University(Base):
    __tablename__ = "universities"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String(150), unique=True, nullable=False)
    location: Mapped[str | None] = mapped_column(String(150))


class Employee(Base):
    __tablename__ = "employees"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String(150), nullable=False)
    company: Mapped[str] = mapped_column(String(150), index=True, nullable=False)
    role: Mapped[str] = mapped_column(String(150), index=True, nullable=False)
    university: Mapped[str | None] = mapped_column(String(150), index=True)
    experience_years: Mapped[int] = mapped_column(default=0)
    skills: Mapped[str | None] = mapped_column(String(1000))


class Job(Base):
    __tablename__ = "jobs"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    company: Mapped[str] = mapped_column(String(150), index=True, nullable=False)
    title: Mapped[str] = mapped_column(String(150), index=True, nullable=False)
    location: Mapped[str | None] = mapped_column(String(150))
    experience_level: Mapped[str | None] = mapped_column(String(100))
    required_skills: Mapped[str | None] = mapped_column(String(1000))
