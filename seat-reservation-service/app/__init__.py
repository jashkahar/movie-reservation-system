from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from app.utils.database import db, migrate
from app.routes.seat_routes import seat_routes
from flask import jsonify
import os
from flask_cors import CORS

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    CORS(app)
    env = os.environ.get('FLASK_ENV', 'development')
    
    if env == "production":
        app.config.from_object("config.ProductionConfig")
    else:
        app.config.from_object("config.DevelopmentConfig")
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
    db.init_app(app)
    migrate.init_app(app, db)

    app.register_blueprint(seat_routes, url_prefix='/api')

    @app.errorhandler(Exception)
    def handle_error(e):
        return jsonify({"error": str(e)}), 500
    
    return app
