from flask import Blueprint, jsonify, request
from app.models import Payment
import random

payment_routes = Blueprint('payment_routes', __name__)

@payment_routes.route('/simulate-payment', methods=['POST'])
def simulate_payment():
    data = request.json

    # Extract data from request
    ticket_id = data.get('ticket_id')
    amount = data.get('amount')

    if not all([ticket_id, amount]):
        return jsonify({"error": "Missing required fields"}), 400

    # Save payment to database
    try:
        payment = Payment.create_payment(ticket_id, amount, request.args.get('status', 'Success'))
        return jsonify({
            "message": "Payment processed successfully!",
            "payment_id": payment.id,
            "status": payment.status
        }), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500