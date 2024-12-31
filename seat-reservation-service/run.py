from app import create_app
import os
from app.utils.database import db


app = create_app()

with app.app_context():
    db.create_all()  # Create tables

if __name__ == "__main__":
    environment = os.getenv('FLASK_ENV', 'local')
    print(f"Running in {environment} environment")
    app.run(debug=True)