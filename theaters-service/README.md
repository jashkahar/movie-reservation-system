# Theaters Service

The Theaters Service is a Spring Boot application that provides RESTful APIs for managing theaters, auditoriums, and seats in a movie reservation system.

## Table of Contents

- [Prerequisites](#prerequisites)
- [Setup](#setup)
- [Running the Application](#running-the-application)
- [API Endpoints](#api-endpoints)
  - [Theater Endpoints](#theater-endpoints)
  - [Auditorium Endpoints](#auditorium-endpoints)
  - [Seat Endpoints](#seat-endpoints)
- [Database Configuration](#database-configuration)

## Prerequisites

- Java 17
- Maven
- PostgreSQL

## Setup

1. Clone the repository:

   ```sh
   git clone https://github.com/your-username/movie-reservation-system.git
   cd movie-reservation-system/theaters-service
   ```

2. Configure the database connection in `src/main/resources/application.properties`:

   ```properties
   spring.datasource.url=jdbc:postgresql://localhost:5433/theater_service
   spring.datasource.username=postgres
   spring.datasource.password=your_password
   spring.jpa.hibernate.ddl-auto=update
   spring.jpa.properties.hibernate.dialect=org.hibernate.dialect.PostgreSQLDialect
   ```

3. Install the dependencies and build the project:
   ```sh
   mvn clean install
   ```

## Running the Application

1. Start the PostgreSQL database.

2. Run the Spring Boot application:

   ```sh
   mvn spring-boot:run
   ```

3. The application will start on port `8082` by default.

## API Endpoints

### Theater Endpoints

- **Get all theaters**

  ```http
  GET /theaters
  ```

  Response:

  ```json
  [
      {
          "id": 1,
          "name": "AMC",
          "location": "123 Main St",
          "contactDetails": "123-456-7890",
          "auditoriums": []
      },
      ...
  ]
  ```

- **Get theater by ID**

  ```http
  GET /theaters/{id}
  ```

  Response:

  ```json
  {
    "id": 1,
    "name": "AMC",
    "location": "123 Main St",
    "contactDetails": "123-456-7890",
    "auditoriums": []
  }
  ```

- **Add a new theater**

  ```http
  POST /theaters
  ```

  Request body:

  ```json
  {
    "name": "AMC",
    "location": "123 Main St",
    "contactDetails": "123-456-7890"
  }
  ```

- **Delete a theater**
  ```http
  DELETE /theaters/{id}
  ```

### Auditorium Endpoints

- **Get all auditoriums**

  ```http
  GET /auditoriums
  ```

  Response:

  ```json
  [
      {
          "id": 1,
          "screenType": "IMAX",
          "seatingCapacity": 200,
          "theaterName": "AMC"
      },
      ...
  ]
  ```

- **Get auditorium by ID**

  ```http
  GET /auditoriums/{id}
  ```

  Response:

  ```json
  {
    "id": 1,
    "screenType": "IMAX",
    "seatingCapacity": 200,
    "theaterName": "AMC"
  }
  ```

- **Get auditoriums by theater ID**

  ```http
  GET /auditoriums/theater/{theaterId}
  ```

  Response:

  ```json
  [
      {
          "id": 1,
          "screenType": "IMAX",
          "seatingCapacity": 200,
          "theaterName": "AMC"
      },
      ...
  ]
  ```

- **Add a new auditorium**

  ```http
  POST /auditoriums
  ```

  Request body:

  ```json
  {
    "screenType": "IMAX",
    "seatingCapacity": 200,
    "theater": {
      "id": 1
    }
  }
  ```

- **Delete an auditorium**
  ```http
  DELETE /auditoriums/{id}
  ```

### Seat Endpoints

- **Get all seats**

  ```http
  GET /seats
  ```

  Response:

  ```json
  [
      {
          "id": 1,
          "row": "A",
          "seatColumn": 1,
          "type": "VIP",
          "status": "Available",
          "auditorium": {}
      },
      ...
  ]
  ```

- **Get seat by ID**

  ```http
  GET /seats/{id}
  ```

  Response:

  ```json
  {
    "id": 1,
    "row": "A",
    "seatColumn": 1,
    "type": "VIP",
    "status": "Available",
    "auditorium": {}
  }
  ```

- **Add a new seat**

  ```http
  POST /seats
  ```

  Request body:

  ```json
  {
    "row": "A",
    "seatColumn": 1,
    "type": "VIP",
    "status": "Available",
    "auditorium": {
      "id": 1
    }
  }
  ```

- **Delete a seat**
  ```http
  DELETE /seats/{id}
  ```

## Database Configuration

Ensure that your PostgreSQL database is running and accessible. Update the database connection details in the `application.properties` file as needed.

```properties
spring.datasource.url=jdbc:postgresql://localhost:5433/theater_service
spring.datasource.username=postgres
spring.datasource.password=your_password
spring.jpa.hibernate.ddl-auto=update
spring.jpa.properties.hibernate.dialect=org.hibernate.dialect.PostgreSQLDialect
```

Replace `your_password` with the actual password for your PostgreSQL database.
