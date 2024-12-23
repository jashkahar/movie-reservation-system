# Movies Service

The application will start on port 8081 by default.

## API Endpoints

The following endpoints are available:

- **GET /movies**: Retrieve all movies or search movies by genre, language, keyword, or nowshowing status
- **POST /movies**: Add a new movie

## Example Requests

### GET /movies

Retrieve all movies:

```sh
curl -X GET http://localhost:8081/movies
```

Search movies by genre:

```sh
curl -X GET "http://localhost:8081/movies?genre=Action"
```

Search movies by language:

```sh
curl -X GET "http://localhost:8081/movies?language=English"
```

Search movies by keyword:

```sh
curl -X GET "http://localhost:8081/movies?keyword=Avengers"
```

Search movies by nowshowing status:

```sh
curl -X GET "http://localhost:8081/movies?nowshowing=true"
```

### POST /movies

Add a new movie:

```sh
curl -X POST http://localhost:8081/movies -H "Content-Type: application/json" -d '{
  "title": "Movie Title",
  "description": "Movie Description",
  "genre": "Genre",
  "director": "Director Name",
  "duration": 120,
  "language": "English",
  "posterUrl": "http://example.com/poster.jpg",
  "nowshowing": true,
  "releaseDate": "2024-12-22"
}'
```

## Configuration

The application can be configured using the `application.properties` file located in the `src/main/resources` directory. Here are some of the key properties:

- `spring.application.name`: The name of the application
- `spring.datasource.url`: The URL of the database
- `spring.datasource.username`: The username for the database
- `spring.datasource.password`: The password for the database
- `spring.jpa.hibernate.ddl-auto`: The Hibernate DDL auto configuration
- `spring.jpa.properties.hibernate.dialect`: The Hibernate dialect
- `server.port`: The port on which the application will run
- `spring.flyway.enabled`: Enable Flyway migrations
- `spring.flyway.locations`: The location of the Flyway migration scripts

## How to Consume

To consume the API, you can use tools like `curl` or Postman. Here are some example commands:

### Using curl

```sh
# Retrieve all movies
curl -X GET http://localhost:8081/movies

# Add a new movie
curl -X POST http://localhost:8081/movies -H "Content-Type: application/json" -d '{
  "title": "Movie Title",
  "description": "Movie Description",
  "genre": "Genre",
  "director": "Director Name",
  "duration": 120,
  "language": "English",
  "posterUrl": "http://example.com/poster.jpg",
  "nowshowing": true,
  "releaseDate": "2024-12-22"
}'
```

### Using Postman

1. Open Postman.
2. Create a new request.
3. Set the request type to GET or POST.
4. Enter the URL (e.g., `http://localhost:8081/movies`).
5. For POST requests, set the body to raw JSON and provide the movie details.
