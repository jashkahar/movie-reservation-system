from app.utils.database import db

class Ticket(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, nullable=False)
    movie_id = db.Column(db.Integer, nullable=False)
    showtime_id = db.Column(db.Integer, nullable=False)
    seat_numbers = db.Column(db.String, nullable=False)  # Comma-separated seat numbers
    status = db.Column(db.String, default='Booked')  # Booked or Cancelled
    created_at = db.Column(db.DateTime, server_default=db.func.now())

    @staticmethod
    def create_ticket(user_id, movie_id, showtime_id, seat_numbers):
        ticket = Ticket(
            user_id=user_id,
            movie_id=movie_id,
            showtime_id=showtime_id,
            seat_numbers=seat_numbers
        )
        db.session.add(ticket)
        db.session.commit()
        return ticket

    @staticmethod
    def get_ticket(ticket_id):
        return Ticket.query.get(ticket_id)


class Payment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    ticket_id = db.Column(db.Integer, db.ForeignKey('ticket.id'), nullable=False)
    status = db.Column(db.String, default='Pending')  # Pending, Success, or Failure
    amount = db.Column(db.Float, nullable=False)
    created_at = db.Column(db.DateTime, server_default=db.func.now())

    @staticmethod
    def create_payment(ticket_id, amount, status='Pending'):
        payment = Payment(ticket_id=ticket_id, amount=amount, status=status)
        db.session.add(payment)
        db.session.commit()
        return payment
