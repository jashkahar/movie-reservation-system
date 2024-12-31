from flask import Flask
from app.utils.database import db, migrate
from app.routes.seat_routes import seat_routes
from flask import jsonify
import os
from flask_cors import CORS
from config import LocalConfig, ProductionConfig

def create_app():
    app = Flask(__name__)
    CORS(app)
    env = os.environ.get('FLASK_ENV', 'local')
    
    if env == "production":
        app.config.from_object(ProductionConfig)
    else:
        app.config.from_object(LocalConfig)
    
    db.init_app(app)
    migrate.init_app(app, db)

    app.register_blueprint(seat_routes)

    @app.errorhandler(Exception)
    def handle_error(e):
        return jsonify({"error": str(e)}), 500
    
    return app
