import requests
from src.config import API_KEY

BASE_URL = "https://api.themoviedb.org/3"


def search_movie(title):
    url = f"{BASE_URL}/search/movie"
    params = {
        "api_key": API_KEY,
        "query": title,
        "language": "pl-PL"
    }
    response = requests.get(url, params=params)
    response.raise_for_status()
    return response.json()["results"]


POSTER_URL = "https://image.tmdb.org/t/p/w500"
def get_movie(results):
    if not results:
        return None
    movie = results[0]
    return {
        "tmdb_id": movie["id"],
        "poster": POSTER_URL + movie["poster_path"] if movie["poster_path"] else None,
        "title": movie["title"],
        "overview": movie["overview"],
        "rating": movie["vote_average"],
        "release_date": movie["release_date"],
        "language": movie["original_language"]
    }



