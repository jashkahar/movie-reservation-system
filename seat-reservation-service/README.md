# Seat Reservation Service

This is a Flask-based microservice for managing seat reservations in a movie reservation system.

## Features

- Manage theaters, seats, shows, and reservations.
- RESTful API endpoints for interacting with the service.
- Database migrations using Flask-Migrate.
- Environment-specific configurations for development and production.

## Setup

### Prerequisites

- Python 3.8+
- PostgreSQL
- Virtualenv (optional but recommended)

### Installation

1. Clone the repository:

   ```sh
   git clone https://github.com/yourusername/movie-reservation-system.git
   cd movie-reservation-system/seat-reservation-service
   ```

2. Create and activate a virtual environment:

   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the dependencies:

   ```sh
   pip install -r requirements.txt
   ```

4. Set up the environment variables:

   ```sh
   cp .env.example .env
   ```

5. Update the `.env` file with your database credentials and other configurations.

6. Run the database migrations:
   ```sh
   flask db upgrade
   ```

### Running the Service

1. Start the Flask development server:

   ```sh
   flask run
   ```

2. The service will be available at `http://localhost:5000`.

## Usage

### API Endpoints

- `GET /api/health` - Health check endpoint.
- `GET /api/seats` - Retrieve all seats.

### Example Request

```sh
curl http://localhost:5000/api/seats
```
