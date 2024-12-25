from flask import Blueprint, jsonify, request
from app.models import Ticket

ticket_routes = Blueprint('ticket_routes', __name__)

@ticket_routes.route('/book-ticket', methods=['POST'])
def book_ticket():
    data = request.json

    # Extract data from request
    user_id = data.get('user_id')
    movie_id = data.get('movie_id')
    showtime_id = data.get('showtime_id')
    seat_numbers = data.get('seat_numbers')  # Example: "A1,A2,A3"

    if not all([user_id, movie_id, showtime_id, seat_numbers]):
        return jsonify({"error": "Missing required fields"}), 400

    # Save ticket to database
    try:
        ticket = Ticket.create_ticket(user_id, movie_id, showtime_id, seat_numbers)
        return jsonify({
            "message": "Ticket booked successfully!",
            "ticket_id": ticket.id,
            "status": ticket.status
        }), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500
