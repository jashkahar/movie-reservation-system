# User Service

This is the User Service for the Movie Reservation System. It handles user registration, authentication, and user management.

## Features

- User registration
- User authentication using JWT
- CRUD operations for user management

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/movie-reservation-system.git
   cd movie-reservation-system/users-service
   ```

2. Create a virtual environment and activate it:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Apply the migrations:

   ```bash
   python manage.py migrate
   ```

5. Create a superuser:

   ```bash
   python manage.py createsuperuser
   ```

6. Run the development server:
   ```bash
   python manage.py runserver
   ```

## API Endpoints

- `POST /api/accounts/register/` - Register a new user
- `POST /api/accounts/token/` - Obtain JWT token
- `POST /api/accounts/token/refresh/` - Refresh JWT token
- `GET /api/accounts/user/` - Get all users
- `PUT /api/accounts/user/<int:pk>/` - Update a user
- `PATCH /api/accounts/user/<int:pk>/` - Partially update a user
- `DELETE /api/accounts/user/<int:pk>/` - Delete a user

## Configuration

- The Django settings are located in `user_service/settings.py`.
- The custom user model is defined in `accounts/models.py`.
