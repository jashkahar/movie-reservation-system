#!/bin/bash

# Set Flask environment
export FLASK_APP=run.py:create_app
export FLASK_ENV=production

# Run database migrations
if [ ! -d "migrations" ] || [ -z "$(ls -A migrations)" ]; then
    flask db init || true
fi
flask db migrate -m "Initial migration" || true
flask db upgrade || true

# Start the Flask application
exec flask run --host=0.0.0.0 --port=8083
