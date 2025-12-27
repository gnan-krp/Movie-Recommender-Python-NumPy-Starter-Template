from src.data_loader import load_movies, load_ratings
from src.user_item_matrix import create_user_item_matrix
from src.collaborative_filtering import recommend_movies
from src.ascii_visuals import ascii_bar_chart
import numpy as np

# Load data
movies = load_movies()
ratings = load_ratings()

# Create user-item matrix
user_item_matrix = create_user_item_matrix(ratings)

# Example: Show matrix
print("User-Item Matrix:\n", user_item_matrix)

# Example: Recommend movies for User 1
recommended = recommend_movies(1, user_item_matrix, top_n=3)
print("\nRecommended Movies for User 1:")
for movie in recommended:
    print("-", movie)

# Show ASCII bar chart of sample ratings
ascii_bar_chart(
    [m[1] for m in movies[:4]],
    [5,3,4,2]
)
