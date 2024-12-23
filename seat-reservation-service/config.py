class Config:
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class DevelopmentConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql://seat_user:password123@localhost/seat_reservation'

class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'production_db_connection_string'
