from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from app.utils.database import db, migrate
from app.routes.ticket_routes import ticket_routes
from app.routes.payment_routes import payment_routes
from app.models import Ticket, Payment  # Import models
from flask import jsonify
import os
from flask_cors import CORS


def create_app():
    app = Flask(__name__)
    CORS(app)
    app.config.from_object('config.Config')

    # Initialize extensions
    db.init_app(app)
    migrate.init_app(app, db)

    # Register blueprints
    app.register_blueprint(ticket_routes)
    app.register_blueprint(payment_routes)

    @app.errorhandler(Exception)
    def handle_error(e):
        return jsonify({"error": str(e)}), 500
    
    return app