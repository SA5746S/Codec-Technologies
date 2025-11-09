# 🎥 Movie Recommendation System
# Technique: Content-Based Filtering

import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# 🔹 Step 1: Create a sample movie dataset
data = {
    'title': [
        'The Avengers', 'Iron Man', 'Captain America', 'Thor', 
        'The Dark Knight', 'Man of Steel', 'Spider-Man', 'Doctor Strange'
    ],
    'genre': [
        'Action Adventure Sci-Fi', 'Action Sci-Fi', 'Action Adventure', 'Action Fantasy',
        'Action Crime Drama', 'Action Adventure Sci-Fi', 'Action Fantasy', 'Action Adventure Fantasy'
    ]
}

movies = pd.DataFrame(data)
print("🎬 Movie Dataset:")
print(movies)

# 🔹 Step 2: Convert movie genres/text into numerical features
tfidf = TfidfVectorizer(stop_words='english')
tfidf_matrix = tfidf.fit_transform(movies['genre'])

# 🔹 Step 3: Compute similarity between all movies
cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)

# 🔹 Step 4: Function to recommend movies
def recommend_movie(title, cosine_sim=cosine_sim):
    if title not in movies['title'].values:
        return ["❌ Movie not found in database."]
    
    # Get the index of the movie
    idx = movies[movies['title'] == title].index[0]
    
    # Get similarity scores
    sim_scores = list(enumerate(cosine_sim[idx]))
    
    # Sort movies by similarity score (highest first)
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    
    # Get top 5 similar movies (excluding itself)
    sim_scores = sim_scores[1:6]
    
    # Get movie titles
    movie_indices = [i[0] for i in sim_scores]
    return movies['title'].iloc[movie_indices].tolist()

# 🔹 Step 5: Test the system
print("\n🎯 Recommended Movies for 'Iron Man':")
print(recommend_movie('Iron Man'))

print("\n🎯 Recommended Movies for 'The Dark Knight':")
print(recommend_movie('The Dark Knight'))
