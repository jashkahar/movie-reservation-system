from app.utils.database import db
import os
from flask import Flask
from app.utils.database import db, migrate
from app.routes.ticket_routes import ticket_routes
from app.routes.payment_routes import payment_routes
from app.models import Ticket, Payment  # Import models
from flask import jsonify
import os
from config import LocalConfig, ProductionConfig
from flask_cors import CORS
from app import create_app

app=create_app()

with app.app_context():
    db.create_all()  # Create tables

if __name__ == '__main__':
    environment = os.getenv('FLASK_ENV', 'local')
    print(f"Running in {environment} environment")
    app.run(debug=True)
