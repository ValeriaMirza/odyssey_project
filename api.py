from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import json
from typing import List, Optional, Dict
from data_processing import extract_movie_type, extract_duration_period, extract_name, extract_genre
from scraper import extract_movie_data_for_year  # Import the scraping function and Movie model

app = FastAPI()

# Load the movie data from JSON file
def load_movies():
    try:
        with open('data_storage/movies.json', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

def fetch_movie_data_for_year(year: int):
    response_movies = extract_movie_data_for_year(year)
    movies = []
    for movie in response_movies:
        movie_type = extract_movie_type(movie)
        duration_period = extract_duration_period(movie)
        name = extract_name(movie, movie_type)
        genre = extract_genre(movie)
        movies.append(
            {
                'name': name,
                'type': movie_type,
                'duration': duration_period,
                'genre': genre
            }
        )
    return movies

# Save the movie data to JSON file
def save_movies(movies):
    with open('data_storage/movies.json', 'w') as file:
        json.dump(movies, file, indent=4)

@app.get("/movies", response_model=Dict[int, List[Dict]])
def get_movies():
    return load_movies()

@app.get("/movies/{year}", response_model=List[Dict])
def get_movies_by_year(year: int):
    movies = load_movies()
    if str(year) in movies:
        return movies[str(year)]
    raise HTTPException(status_code=404, detail="Movies not found for this year")

@app.post("/movies/{year}", response_model=List[Dict])
def add_movies_by_year(year: int):
    movies = load_movies()
    if str(year) in movies:
        raise HTTPException(status_code=400, detail="Movies for this year already exist")
    
    new_movies = fetch_movie_data_for_year(year)
    movies[str(year)] = new_movies
    save_movies(movies)
    return new_movies

@app.put("/movies/{year}", response_model=List[Dict])
def update_movie(year: int):
    movies = load_movies()
    new_movies = fetch_movie_data_for_year(year)
    movies[str(year)] = new_movies
    save_movies(movies)
    return new_movies

@app.delete("/movies/{year}/{name}", response_model=Dict)
def delete_movie(year: int, name: str):
    movies = load_movies()
    year_str = str(year)
    if year_str not in movies:
        raise HTTPException(status_code=404, detail="Movies not found for this year")

    for i, movie in enumerate(movies[year_str]):
        if movie['name'].lower() == name.lower():
            deleted_movie = movies[year_str].pop(i)
            save_movies(movies)
            return deleted_movie
    
    raise HTTPException(status_code=404, detail="Movie not found")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
