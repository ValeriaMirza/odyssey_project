import requests
from bs4 import BeautifulSoup

def extract_movie_data_for_year(year: int) -> list:
    """Fetch the most popular movies in a given year

    Args:
        year (int): the year for which to fetch the most popular movies

    Returns:
        list: the most popular movies in the given year
    """
    url = f'https://www.google.com/search?q=popular+movies+in+{year}'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        movie_titles = soup.find_all(class_='UnFsfe cyKJce ZvGeOb')
        movies = [title.get_text() for title in movie_titles]
        return movies
    else:
        print("Failed to fetch data")
        return []
