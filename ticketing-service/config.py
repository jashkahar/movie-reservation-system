import os

class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL", "postgresql://ticket_user:password123@localhost:5433/ticketing_service")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
