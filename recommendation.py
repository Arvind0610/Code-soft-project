import pandas as pd
import os
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def load_data():
    current_folder = os.path.dirname(__file__)
    file_path = os.path.join(current_folder, "movies.csv")
    data = pd.read_csv(file_path)
    return data


def create_similarity_matrix(data):
    vectorizer = CountVectorizer()
    genre_matrix = vectorizer.fit_transform(data['genre'])
    similarity = cosine_similarity(genre_matrix)
    return similarity


def recommend_movie(movie_name, data, similarity_matrix):
    if movie_name not in data['title'].values:
        print("❌ Movie not found in database.")
        return

    movie_index = data[data['title'] == movie_name].index[0]
    similarity_scores = list(enumerate(similarity_matrix[movie_index]))
    similarity_scores = sorted(similarity_scores, key=lambda x: x[1], reverse=True)

    print(f"\n🎬 Recommended movies for '{movie_name}':\n")

    for i in similarity_scores[1:6]:
        print("✅", data.iloc[i[0]]['title'])


def main():
    print("===================================")
    print("   🎥 MOVIE RECOMMENDATION SYSTEM ")
    print("===================================\n")

    data = load_data()
    similarity_matrix = create_similarity_matrix(data)

    user_movie = input("Enter a movie name: ")
    recommend_movie(user_movie, data, similarity_matrix)


if __name__ == "__main__":
    main()
