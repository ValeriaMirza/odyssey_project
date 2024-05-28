import re
from scraper import extract_movie_data_for_year
def extract_movie_type(entry: str) -> str:
    """Extract the type of the movie from the entry

    Args:
        entry (str): the entry from which to extract the type

    Returns:
        str: the type of the movie
    """
    movie_types = ['PG-13', 'NC-17', 'PG', 'R', 'G']
    for i in movie_types:
        if i in entry:
            return i
    return "N/A"


def extract_duration_period(entry: str) -> tuple:
    """Extract the duration of the movie from the entry

    Args:
        entry (str): the entry from which to extract the duration

    Returns:
        tuple: the duration of the movie
    """
    match = re.search(r'(?:G|PG(?:-13)?|R|NC-17)(\d+)\s*h\s*(\d+)\s*min', entry)
    if match:
        hours = int(match.group(1))
        minutes = int(match.group(2))
        return (hours, minutes)
    else:
        return (0, 0) 


def extract_name(entry: str, movie_type="Unknown") -> str:
    """Extract the name of the movie from the entry
    
    Args:
        entry (str): the entry from which to extract the name
        movie_type (str): the type of the movie
        
    Returns:
        str: the name of the movie
    """
    pattern = re.compile(r'^([^0-9]+)')
    match = pattern.match(entry)
    if match:
        modified_entry = match.group(1)
        last_letter = modified_entry[-1]
        if last_letter in ['R', 'G']:
            modified_entry = modified_entry[:-1]
        elif modified_entry[-2:] == 'PG':
            modified_entry = modified_entry[:-2]
        elif modified_entry[-3:] == 'PG-':
            modified_entry = modified_entry[:-3]
        return modified_entry.strip()
    else:
        return "N/A"

def extract_genre(entry: str) -> str:
    """Extract the genre of the movie from the entry
    
    Args:
        entry (str): the entry from which to extract the genre
        
    Returns:
        str: the genre of the movie
    """
    genres = ['Thriller', 'Dramă', 'Dragoste', 'De comedie', 'Istorie', 'Acțiune', 'Anime','Narațiune', 'De groază']
    for genre in genres:
        if genre in entry:
            return genre
    return "N/A"
