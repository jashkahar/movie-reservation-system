import requests
import psycopg2

# TMDb API configuration
API_KEY = "your_tmdb_api_key"
BASE_URL = "https://api.themoviedb.org/3"
MOVIE_URL = f"{BASE_URL}/movie/popular"

# Database configuration
DB_CONFIG = {
    "dbname": "movies_db",
    "user": "postgres",
    "password": "your_password",
    "host": "localhost",
    "port": "5432"
}

def fetch_movies():
    params = {"api_key": API_KEY, "language": "en-US", "page": 1}
    response = requests.get(MOVIE_URL, params=params)
    response.raise_for_status()
    return response.json().get("results", [])

def insert_movies(movies):
    conn = psycopg2.connect(**DB_CONFIG)
    cursor = conn.cursor()
    for movie in movies:

        title = movie["title"]
        description = movie["overview"]
        genre = ", ".join([g["name"] for g in movie.get("genre_ids", [])])
        director = "Unknown"  # Use another API call if needed for director
        duration = 120  # Default or from another API
        language = movie["original_language"]
        poster_url = f"https://image.tmdb.org/t/p/w500{movie['poster_path']}"
        now_showing = True  # Custom logic for now showing
        release_date = movie["release_date"]

        query = """
        INSERT INTO movies (title, description, genre, director, duration, language, poster_url, now_showing, release_date)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
        """
        cursor.execute(query, (title, description, genre, director, duration, language, poster_url, now_showing, release_date))
    conn.commit()
    cursor.close()
    conn.close()

if __name__ == "__main__":
    movies = fetch_movies()
    insert_movies(movies)
    print("Movies inserted successfully.")
