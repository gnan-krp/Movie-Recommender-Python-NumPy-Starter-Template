from data.movies import movies
from data.ratings import ratings
import numpy as np

def load_movies():
    return np.array(movies)

def load_ratings():
    return np.array(ratings)
