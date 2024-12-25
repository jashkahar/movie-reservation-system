from app import create_app
from app.utils.database import db
from app.models import Ticket, Payment  # Import models

app = create_app()

with app.app_context():
    db.create_all()  # Create tables

if __name__ == '__main__':
    app.run(debug=True)
