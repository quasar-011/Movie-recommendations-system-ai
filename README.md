# Movie Recommendation System

This Python script implements a simple movie recommendation system based on user input and movie metadata.

## Requirements

- Python 3.x
- pandas
- fuzzywuzzy

## Installation

1. Install Python 3.x from [Python's official website](https://www.python.org/downloads/).
2. Install required Python packages using pip:
   ```
   pip install pandas fuzzywuzzy
   ```

## Usage

1. Clone or download this repository to your local machine.
2. Ensure you have the required dataset files (`movie.csv`, `tag.csv`, `rating.csv`) in the specified directory (`/home/quasar_011/Developer/datasets/movieLens/`). You can replace these paths in the code according to your dataset location.
3. Open a terminal or command prompt and navigate to the directory containing the downloaded files.
4. Run the script using the following command:
   ```
   python movie_recommendation.py
   ```
5. Follow the prompts:
   - Enter your favorite movie genre.
   - Enter movie titles along with your rating (out of 5), separated by a comma. Press Enter to stop adding movies.
6. Once you've entered your input, the script will display recommended movies based on your preferences.

## File Descriptions

- `movie_recommendation.py`: The main Python script containing the movie recommendation logic.
- `movie.csv`: Dataset containing movie information such as movie ID, title, and genres.
- `tag.csv`: Dataset containing tags associated with movies.
- `rating.csv`: Dataset containing user ratings for movies.

## Functionality

- **read_data(file_path)**: Reads the CSV file located at the specified path using pandas and returns a DataFrame. If the file is not found, it prints an error message and returns an empty DataFrame.
- **get_user_input()**: Prompts the user to enter their favorite movie genre and a list of movies along with their ratings.
- **match_movies_with_tags(user_movies_input, favorite_genre, movies_data, tags_data, ratings_data)**: Matches user-input movies with similar movies based on common tags and returns a DataFrame of recommended movies.
- **display_recommendations(recommended_movies, movies_data)**: Displays the top recommended movies along with their ratings.

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or create a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

Feel free to customize this README according to your project's specifics and additional information you'd like to provide!
