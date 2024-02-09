from flask import Flask, render_template, jsonify

app = Flask(__name__)

# Sample movie data
movies = [
    {"id": 1, "title": "Movie 1", "poster": "movie1.jpg"},
    {"id": 2, "title": "Movie 2", "poster": "movie2.jpg"},
    {"id": 3, "title": "Movie 3", "poster": "movie3.jpg"},
    # Add more movies as needed
]

# Sample recommendation function
def get_recommendations(movie_id):
    # Implement your recommendation logic here
    recommendations = ["Recommendation 1", "Recommendation 2", "Recommendation 3"]
    return recommendations

@app.route('/')
def index():
    return render_template('index.html', movies=movies)

@app.route('/recommend/<int:movie_id>')
def recommend(movie_id):
    recommendations = get_recommendations(movie_id)
    return jsonify(recommendations)

if __name__ == '__main__':
    app.run(debug=True)
