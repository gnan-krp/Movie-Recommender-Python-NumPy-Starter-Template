import numpy as np
from data_loader import load_movies

def cosine_similarity(u1, u2):
    if np.linalg.norm(u1) == 0 or np.linalg.norm(u2) == 0:
        return 0
    return np.dot(u1, u2) / (np.linalg.norm(u1) * np.linalg.norm(u2))

def recommend_movies(user_id, user_item_matrix, top_n=3):
    user_ratings = user_item_matrix[user_id-1]
    similarities = []
    
    for i in range(user_item_matrix.shape[0]):
        if i != user_id-1:
            sim = cosine_similarity(user_ratings, user_item_matrix[i])
            similarities.append((i, sim))
    
    similarities.sort(key=lambda x: x[1], reverse=True)
    top_user = similarities[0][0]
    
    recommended = []
    for i, rating in enumerate(user_item_matrix[top_user]):
        if user_ratings[i] == 0 and rating > 0:
            recommended.append((i, rating))
    
    recommended.sort(key=lambda x: x[1], reverse=True)
    
    movie_list = load_movies()
    return [movie_list[i][1] for i, r in recommended[:top_n]]
