from sqlalchemy import create_engine

from app.core.config import settings
from app.db.database import Base
from app.db import models  # noqa: F401


def init_db():
    engine = create_engine(settings.database_url, pool_pre_ping=True)
    Base.metadata.create_all(bind=engine)
    print("Database tables created successfully.")


if __name__ == "__main__":
    init_db()
