from tmdbv3api import TMDb, Movie

tmdb = TMDb()
tmdb.api_key = '1e4e745b6f4f8b64f49942ced0f5551c'

movie = Movie()

def fetch_movie_details(movie_id):
    details = movie.details(movie_id)
    return {
        'title': details.title,
        'overview': details.overview,
        'poster_path': f"https://image.tmdb.org/t/p/w500{details.poster_path}"
    }

if __name__ == "__main__":
    movie_id = 550  # Example movie ID (Fight Club)
    print(fetch_movie_details(movie_id))
