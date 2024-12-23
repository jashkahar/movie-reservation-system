from app.utils.database import db
from datetime import datetime

class Theater(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    location = db.Column(db.String(200), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

class Seat(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    theater_id = db.Column(db.Integer, nullable=False)  # Placeholder until Theater Service is ready
    row = db.Column(db.String(10), nullable=False)
    number = db.Column(db.Integer, nullable=False)
    type = db.Column(db.String(50), nullable=False)  # e.g., regular, VIP
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

class Show(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    movie_id = db.Column(db.Integer, nullable=False)  # Placeholder for integration
    theater_id = db.Column(db.Integer, db.ForeignKey('theater.id'), nullable=False)
    start_time = db.Column(db.DateTime, nullable=False)
    end_time = db.Column(db.DateTime, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

class Reservation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    show_id = db.Column(db.Integer, nullable=False)  # Placeholder until Show Service is ready
    seat_id = db.Column(db.Integer, db.ForeignKey('seat.id'), nullable=False)
    user_id = db.Column(db.Integer, nullable=False)  # Placeholder until User Service is ready
    status = db.Column(db.String(50), nullable=False)  # e.g., locked, reserved, cancelled
    locked_until = db.Column(db.DateTime, nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
