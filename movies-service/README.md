# Movies Service

The application will start on port 8081 by default.

## API Endpoints

The following endpoints are available:

- **GET /movies**: Retrieve all movies
- **POST /movies**: Add a new movie

## Example Requests

### GET /movies

### POST /movies

## Configuration

The application can be configured using the `application.properties` file located in the `src/main/resources` directory. Here are some of the key properties:

## How to Consume

To consume the API, you can use tools like `curl` or Postman. Here are some example commands:

### Using curl

```sh
# Retrieve all movies
curl -X GET http://localhost:8081/movies

# Add a new movie
curl -X POST http://localhost:8081/movies -H "Content-Type: application/json" -d '{"title": "Movie Title", "genre": "Genre", "year": 2021}'
```

### Using Postman

1. Open Postman.
2. Create a new request.
3. Set the request type to GET or POST.
4. Enter the URL (e.g., `http://localhost:8081/movies`).
5. For POST requests, set the body to raw JSON and provide the movie details.
