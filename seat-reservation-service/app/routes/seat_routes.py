from flask import Blueprint, jsonify
from app.models import Seat 

seat_routes = Blueprint('seat_routes', __name__)

@seat_routes.route('/health', methods=['GET'])
def health_check():
    return jsonify({"status": "Seat Reservation Service is running!"})

@seat_routes.route('/seats', methods=['GET'])
def get_seats():
    seats = Seat.query.all()
    return jsonify([{ 
        "id": seat.id,
        "theater_id": seat.theater_id,
        "row": seat.row,
        "number": seat.number,
        "type": seat.type,
        "created_at": seat.created_at
    } for seat in seats])