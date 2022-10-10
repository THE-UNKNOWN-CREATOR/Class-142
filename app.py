from flask import Flask, jsonify, request
from storage import all_movies, liked, disliked, not_watched
from demographic_filtering import output
from content_based_filtering import get_recommendations

app = Flask(__name__)

@app.route("/get-movie")
def get_movie():
    movie_data = {
        "title": all_movies[0][19],
        "poster_link": all_movies[0][27],
        "release_date": all_movies[0][13] or "N/A",
        "duration": all_movies[0][15],
        "rating": all_movies[0][20],
        "overview": all_movies[0][9]
    }
    return jsonify(
        {
            "data":movie_data,
            "status":"success"
        }
    )

@app.route("/like-movie", methods = ["POST"])
def like_movie():
    movies = all_movies[0]
    liked.append(movies)
    all_movies.pop(0)
    return jsonify(
        {
            "status": "success"
        }
    ),201

@app.route("/dislike-movie", methods = ["POST"])
def dislike_movie():
    movies = all_movies[0]
    disliked.append(movies)
    all_movies.pop(0)
    return jsonify(
        {
            "status": "success"
        }
    ),201

@app.route("/not-watched-movie", methods = ["POST"])
def not_watched_movie():
    movies = all_movies[0]
    not_watched.append(movies)
    all_movies.pop(0)
    return jsonify(
        {
            "status": "success"
        }
    ),201

@app.route("/popular-movies")
def popular_movies():
    movie_data = []
    for movie in output:
        _d = {
            "title": movie[0],
            "poster_link": movie[1],
            "release_date": movie[2] or "N/A",
            "duration": movie[3],
            "rating": movie[4],
            "overview": movie[5]
        }
        movie_data.append(_d)
    return jsonify(
        {
            "data": movie_data,
            "status": "successful"
        }
    ),200
    
@app.route("/recomended-movies")
def recomended_movies():
    all_recommended = []
    for liked_movies in liked:
        output = get_recommendations(liked_movies[19])
        for data in output:
            all_recommended.append(data)
    import itertools
    all_recommended.sort()
    all_recommended = list(all_recommended for all_recommended, _ in itertools.groupby(all_recommended))
    movie_data = []
    for movie in all_recommended:
        _d = {
            "title": movie[0],
            "poster_link": movie[1],
            "release_date": movie[2] or "N/A",
            "duration": movie[3],
            "rating": movie[4],
            "overview": movie[5]
        }
        movie_data.append(_d)
    return jsonify(
        {
            "data": movie_data,
            "status": "successful"
        }
    ),200


if __name__ == "__main__":
  app.run()