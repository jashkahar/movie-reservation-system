# Ticketing Service

The Ticketing Service is a part of a movie reservation system that handles ticket booking and payment processing.

## Routes

### Ticket Routes

#### Book Ticket

- **URL:** `/book-ticket`
- **Method:** `POST`
- **Description:** This route handles ticket booking.
- **Request Body:**
  ```json
  {
    "user_id": "string",
    "movie_id": "string",
    "showtime_id": "string",
    "seat_numbers": "string" // Example: "A1,A2,A3"
  }
  ```
- **Responses:**
  - **Success:**
    ```json
    {
      "message": "Ticket booked successfully!",
      "ticket_id": "string",
      "status": "string"
    }
    ```
  - **Error:**
    ```json
    {
      "message": "Error booking ticket",
      "error": "string"
    }
    ```

### Payment Routes

#### Simulate Payment

- **URL:** `/simulate-payment`
- **Method:** `POST`
- **Description:** This route handles payment simulation.
- **Request Body:**
  ```json
  {
    "ticket_id": "string",
    "amount": "number",
    "payment_method": "string"
  }
  ```
- **Query Parameters:**
  - `status` (optional): The status of the payment (default is "Success").
- **Responses:**
  - **Success:**
    ```json
    {
      "message": "Payment processed successfully!",
      "payment_id": "string",
      "status": "Success"
    }
    ```
  - **Error:**
    ```json
    {
      "message": "Payment failed",
      "error": "string"
    }
    ```

## Setup

1. Clone the repository.
2. Install the required dependencies using `pip install -r requirements.txt`.
3. Run the Flask application using `flask run`.

## Dependencies

- Flask
- SQLAlchemy (or any ORM for database interactions)
