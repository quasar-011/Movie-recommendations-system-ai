# Movie Recommendation System using Streamlit

This Streamlit web application provides movie recommendations based on user input and movie metadata.

## Requirements

- Python 3.x
- pandas
- Streamlit
- fuzzywuzzy

## Installation

1. Install Python 3.x from [Python's official website](https://www.python.org/downloads/).
2. Install required Python packages using pip:
   ```
   pip install pandas streamlit fuzzywuzzy
   ```

## Usage

1. Clone or download this repository to your local machine.
2. Ensure you have the required dataset files (`movie.csv`, `tag.csv`, `rating.csv`) in the specified directory (`/home/quasar_011/Developer/datasets/movieLens/`). You can replace these paths in the code according to your dataset location.
3. Open a terminal or command prompt and navigate to the directory containing the downloaded files.
4. Run the Streamlit app using the following command:
   ```
   streamlit run movie_recommendation_app.py
   ```
5. Access the app in your web browser by opening the URL provided in the terminal.

## Functionality

- **read_data(file_path)**: Reads the CSV file located at the specified path using pandas and returns a DataFrame. If the file is not found, it displays an error message.
- **get_user_input()**: Allows the user to enter their favorite movie genre and a list of movies along with their ratings.
- **match_movies_with_tags(user_movies_input, favorite_genre, movies_data, tags_data, ratings_data)**: Matches user-input movies with similar movies based on common tags and returns a DataFrame of recommended movies.
- **display_recommendations(recommended_movies, movies_data)**: Displays the top recommended movies along with their ratings.

## Usage Instructions

1. Enter your favorite movie genre in the provided text input field.
2. Enter movie titles along with their ratings (out of 5) in the text input fields. Press Enter after each input. Click the Submit button when you're done.
3. The app will display recommended movies based on your input.

## File Descriptions

- `movie_recommendation_app.py`: The main Python script containing the Streamlit app logic.
- `movie.csv`: Dataset containing movie information such as movie ID, title, and genres.
- `tag.csv`: Dataset containing tags associated with movies.
- `rating.csv`: Dataset containing user ratings for movies.

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or create a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
