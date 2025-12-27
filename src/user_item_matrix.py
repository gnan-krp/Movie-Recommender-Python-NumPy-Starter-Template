import numpy as np

def create_user_item_matrix(ratings):
    num_users = ratings[:,0].max()
    num_movies = ratings[:,1].max()
    matrix = np.zeros((num_users, num_movies))
    for user_id, movie_id, rating in ratings:
        matrix[user_id-1, movie_id-1] = rating
    return matrix
