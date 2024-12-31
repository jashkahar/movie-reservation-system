import os
import sqlalchemy as sa

class Config:
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class LocalConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql://ticket_user:password123@localhost:5433/ticketing_service'

class ProductionConfig(Config):
    connection_url = sa.engine.URL.create(
        drivername="postgresql",
        username="postgres",
        password="pass@123",
        host="moviereservationpostgresdb",
        database="ticketing_service",
    )
    SQLALCHEMY_DATABASE_URI = connection_url