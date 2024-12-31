from flask import Flask
from app.utils.database import db, migrate
from app.routes.ticket_routes import ticket_routes
from app.routes.payment_routes import payment_routes
from app.models import Ticket, Payment  # Import models
from flask import jsonify
import os
from config import LocalConfig, ProductionConfig
from flask_cors import CORS

def create_app():
    app = Flask(__name__)
    CORS(app)
    environment = os.getenv('FLASK_ENV', 'local')
    print(f"Running in {environment} environment")

    # Load the appropriate config
    if environment == 'production':
        app.config.from_object(ProductionConfig)
    else:
        app.config.from_object(LocalConfig)

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