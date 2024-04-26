import pandas as pd
import streamlit as st
from fuzzywuzzy import process

def read_data(file_path):
    try:
        return pd.read_csv(file_path)
    except FileNotFoundError:
        st.error(f"Error: File '{file_path}' not found.")
        return pd.DataFrame()


# Function to get user input
def get_user_input():
    movies_input = []  # Initialize an empty list
    favorite_genre = st.text_input("Enter your favorite genre:")
    
    st.write("Enter movie titles along with your rating (out of 5), separated by comma (or press Enter to stop adding movies):")
    
    index = 0
    while True:
        movie_input = st.text_input(f"Movie Title and Rating {index + 1} (e.g., 'Movie Title, 4'):", key=f"movie_input_{index}")
        if not movie_input:
            break
        try:
            movie_title, rating = movie_input.split(',')
            rating = float(rating)
            if not 0 <= rating <= 5:  
                st.error("Error: Rating should be between 0 and 5.")
                continue
            movies_input.append((movie_title.strip(), rating))
        except ValueError:
            st.error("Error: Invalid input format. Please enter movie title and rating separated by comma (e.g., 'Movie Title, 4').")
        index += 1
    
    # Add a submit button
    if st.button("Submit"):
        return movies_input, favorite_genre
    else:
        return [], ""  # Return empty values if submit button is not clicked


def match_movies_with_tags(user_movies_input, favorite_genre, movies_data, tags_data, ratings_data):
    recommended_movies = pd.DataFrame(columns=['movieId', 'rating'])
    movie_titles = [movie[0] for movie in user_movies_input]
    movie_ratings = {movie[0]: movie[1] for movie in user_movies_input}
    
    movie_tags = tags_data.groupby('movieId')['tag'].apply(set).to_dict()
    
    genre_tags = tags_data[tags_data['tag'].notna() & tags_data['tag'].str.lower().str.contains(favorite_genre.lower())]['tag']
    genre_tags = set(genre_tags) if not genre_tags.empty else set()
    
    for movie_title in movie_titles:
        match = process.extractOne(movie_title, movies_data['title'])
        matched_movie_title = match[0]
        matched_movie_id = movies_data.loc[movies_data['title'] == matched_movie_title, 'movieId'].values[0]
        
        common_tags = genre_tags.intersection(movie_tags.get(matched_movie_id, set()))
        
        similar_movies_ids = set(tags_data[tags_data['tag'].isin(common_tags)]['movieId'])
        similar_movie_ratings = ratings_data[ratings_data['movieId'].isin(similar_movies_ids)]
        recommended_movies = recommended_movies.append(similar_movie_ratings)
        
    return recommended_movies


# Function to display movie recommendations
def display_recommendations(recommended_movies, movies_data):
    if not recommended_movies.empty:  # Check if DataFrame is not empty
        # Merge recommended movies with movies_data to access ratings
        recommended_movies = pd.merge(recommended_movies, movies_data, on='movieId', how='left')
        top_movies = recommended_movies.groupby('movieId')['rating'].mean().sort_values(ascending=False).head(10)
        for idx, movie_id in enumerate(top_movies.index, start=1):
            movie_info = movies_data[movies_data['movieId'] == movie_id]
            movie_name = movie_info['title'].values[0]
            movie_year = movie_info['title'].values[0][-5:-1]
            movie_rating = top_movies.loc[movie_id]
            st.write(f"{idx}: {movie_name} ({movie_year}), Rating: {movie_rating:.2f}")
    else:
        st.warning("No recommendations found.")

def main():
    movies_data = read_data('/home/quasar_011/Developer/datasets/movieLens/movie.csv')
    tags_data = read_data('/home/quasar_011/Developer/datasets/movieLens/tag.csv')
    ratings_data = read_data('/home/quasar_011/Developer/datasets/movieLens/rating.csv')
    
    if movies_data.empty or tags_data.empty or ratings_data.empty:
        st.error("Error: Failed to load data. Exiting program.")
        return
    
    user_movies_input, favorite_genre = get_user_input()
    
    recommended_movies = match_movies_with_tags(user_movies_input, favorite_genre, movies_data, tags_data, ratings_data)
    
    display_recommendations(recommended_movies, movies_data)

if __name__ == "__main__":
    main()
