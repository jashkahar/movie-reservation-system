# Movie Reservation System

## Project Overview
The **Movie Reservation System** is a microservices-based application designed to allow users to browse movies, search and filter showtimes, reserve seats, and purchase tickets using an external payment gateway (Stripe). This project emulates real-world complexities encountered in web development, focusing on distributed systems, relational data modeling, and transaction management.

---

## Motivation
This project was created to:
- **Learn and practice** modern software engineering concepts:
  - Microservices architecture.
  - RESTful API design.
  - Docker containerization and AWS deployment.
  - Database modeling and ACID transactions.
- **Improve proficiency** in multiple frameworks and languages:
  - **Frontend**: React.js.
  - **Backend**: Spring Boot, Django, Flask.
  - **Database**: PostgreSQL with AWS RDS.
- **Simulate production-grade systems**:
  - Real-time seat booking with concurrency management.
  - Asynchronous service communication using AWS SQS.
  - Scalability and monitoring using AWS ECS (Fargate) and CloudWatch.

This project is an excellent exercise for understanding distributed systems, integrating various technologies, and designing a system with a production-ready mindset.

---

## System Architecture

This system is built using a **microservices architecture**, with each service handling a specific domain of functionality. All services are containerized with Docker and deployed on AWS ECS (Fargate). The frontend interacts with the services through REST APIs, and the database is hosted on AWS RDS (PostgreSQL).

### High-Level Architecture Diagram
```bash
Frontend (React.js) <-> API Gateway <-> Backend Microservices
                       |          |
                  Stripe       PostgreSQL
```

### Microservices Overview
1. **Users Service**:
   - Manages user registration, login, and authentication.
   - Framework: **Django**.
   - Uses JWT for stateless authentication.

2. **Movies Service**:
   - Handles movie metadata and schedules.
   - Framework: **Spring Boot**.
   - Allows filtering movies by genre, date, or actor.

3. **Theaters Service**:
   - Manages theaters and their seating layouts.
   - Framework: **Spring Boot**.
   - Provides APIs to fetch seat layouts.

4. **Seat Reservation Service**:
   - Manages real-time seat reservations.
   - Framework: **Flask**.
   - Ensures concurrency-safe seat bookings.

5. **Ticketing Service**:
   - Handles ticket generation and payment processing.
   - Framework: **Flask**.
   - Integrates with Stripe for secure payments.

---

## Technologies Used

### Frontend
- **React.js**: For building a dynamic, responsive user interface.
- **Bootstrap/Tailwind CSS**: For styling.

### Backend
- **Django**: For the Users Service.
- **Spring Boot**: For the Movies and Theaters Services.
- **Flask**: For the Seat Reservation and Ticketing Services.

### Database
- **PostgreSQL** (via AWS RDS):
  - ACID compliance for transactional data.
  - Relational modeling for movies, theaters, reservations, and tickets.

### Infrastructure
- **Docker**: For containerizing each service.
- **AWS ECS (Fargate)**: For managing and deploying microservices.
- **AWS RDS (PostgreSQL)**: For relational database management.
- **AWS SQS**: For asynchronous communication between services.
- **AWS CloudWatch**: For monitoring and logging.
- **AWS S3 + CloudFront**: For hosting the frontend.

### Payment Gateway
- **Stripe**: For handling secure payments and managing payment intents.

---

## Features

### User-Facing Features
1. **User Registration and Login**:
   - Secure authentication using JWT.
   - Role-based access control (admin vs user).

2. **Movie Search and Filters**:
   - Search movies by title, genre, actor, or date.
   - View detailed movie information and available showtimes.

3. **Seat Selection and Booking**:
   - Interactive seat layout for theaters.
   - Real-time availability and booking confirmation.

4. **Ticket Booking and Payment**:
   - Secure payment processing with Stripe.
   - E-ticket generation with QR codes.

---

## Microservices Overview

Each microservice is responsible for a specific domain, ensuring loose coupling and high cohesion. The system uses REST APIs for communication and follows best practices for scalability and maintainability.

| **Service**              | **Responsibilities**                                                                                   | **Framework**     |
|--------------------------|-------------------------------------------------------------------------------------------------------|-------------------|
| **Users Service**         | User registration, login, JWT-based authentication.                                                  | Django            |
| **Movies Service**        | Manage movie metadata and schedules.                                                                 | Spring Boot       |
| **Theaters Service**      | Manage theaters and seating layouts.                                                                 | Spring Boot       |
| **Seat Reservation Service** | Real-time seat booking, concurrency management.                                                      | Flask             |
| **Ticketing Service**     | Secure payments with Stripe, e-ticket generation.                                                    | Flask             |

---

## Core Database Schema

| **Table Name**    | **Description**                                                                                           |
|--------------------|---------------------------------------------------------------------------------------------------------|
| `Users`            | Stores user data (e.g., username, email, hashed password).                                               |
| `Movies`           | Stores movie metadata (e.g., title, genre, duration, actors).                                            |
| `Theaters`         | Stores theater data (e.g., name, location, capacity).                                                   |
| `Seats`            | Maps theater seating layout (row, column, availability).                                                |
| `Schedules`        | Maps movies to showtimes and theaters.                                                                  |
| `Reservations`     | Tracks user seat reservations.                                                                          |
| `Tickets`          | Tracks ticket sales and payment statuses.                                                              |

---

## How to Run Locally

### Prerequisites
- Docker installed on your machine.
- Node.js and npm for frontend development.
- PostgreSQL installed locally for testing the database.

### Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/movie-reservation-system.git
   cd movie-reservation-system
   ```
2. Start the services:
  - Run the services locally using Docker Compose
  ```bash
  docker-compose up
  ```
3. Access the services:
    Frontend: `http://localhost:3000`
    Users Service: `http://localhost:8000`
    Movies Service: `http://localhost:8081`
    Other services are accessible at their respective ports.

4. Mock data:
    - Use the provided SQL scripts in the infra/ folder to populate the database with mock data.

---
### Future Enhancements
1. Admin Dashboard:
    - Allow admins to manage movies, theaters, and schedules.
2. Recommendation Engine:
    - Suggest movies based on user preferences and viewing history.
3. Real-Time Updates:
    - Implement WebSockets for live seat availability updates.

---

### Learning Outcomes
1. Microservices Architecture: Designing, deploying, and managing distributed systems.
2. Database Modeling: Structuring relational data for scalability and efficiency.
3. RESTful API Design: Creating clean, maintainable APIs for service communication.
4. DevOps Practices: Using Docker, AWS ECS, and CI/CD pipelines.
5. Frontend Development: Building a modern, responsive UI with React.js.
6. Payment Integration: Using Stripe to handle real-world payment workflows.

---

### Contributions
This project is for learning purposes, but contributions are welcome! Please feel free to fork the repository, submit pull requests, or open issues to suggest improvements.
