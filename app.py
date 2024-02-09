from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Dummy user data (replace this with your actual user database)
users = {
    "user1": {"password": "password1", "projects": ["Project A", "Project B"]},
    "user2": {"password": "password2", "projects": ["Project C", "Project D"]}
}

# Dummy project data (replace this with your actual project database)
projects = {
    "Project A": {"description": "Description of Project A"},
    "Project B": {"description": "Description of Project B"},
    "Project C": {"description": "Description of Project C"},
    "Project D": {"description": "Description of Project D"}
}

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/login', methods=['GET', 'POST'])  # Allow both GET and POST requests
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username in users and users[username]["password"] == password:
            # Successful login
            return redirect(url_for('dashboard', username=username))
        else:
            # Failed login
            return render_template('login.html', message="Invalid username or password")
    else:
        # If GET request, render the login page
        return render_template('login.html')

@app.route('/signup')
def signup():
    return render_template('signup.html')

@app.route('/dashboard/<username>')
def dashboard(username):
    user_projects = users[username]["projects"]
    recommended_projects = [projects[project] for project in user_projects]
    return render_template('dashboard.html', username=username, projects=recommended_projects)

if __name__ == '__main__':
    app.run(debug=True)



''' from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Dummy user data (replace this with your actual user database)
users = {
    "user1": {"password": "password1", "projects": ["Project A", "Project B"]},
    "user2": {"password": "password2", "projects": ["Project C", "Project D"]}
}

# Dummy project data (replace this with your actual project database)
projects = {
    "Project A": {"description": "Description of Project A"},
    "Project B": {"description": "Description of Project B"},
    "Project C": {"description": "Description of Project C"},
    "Project D": {"description": "Description of Project D"}
}

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/login', methods=['GET', 'POST'])  # Allow both GET and POST requests
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username in users and users[username]["password"] == password:
            # Successful login
            return redirect(url_for('dashboard', username=username))
        else:
            # Failed login
            return render_template('login.html', message="Invalid username or password")
    else:
        # If GET request, render the login page
        return render_template('login.html')

@app.route('/signup')
def signup():
    return render_template('signup.html')

@app.route('/dashboard/<username>')
def dashboard(username):
    user_projects = users[username]["projects"]
    recommended_projects = [projects[project] for project in user_projects]
    return render_template('dashboard.html', username=username, projects=recommended_projects)

if __name__ == '__main__':
    app.run(debug=True)

 '''

''' from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Dummy user data (replace this with your actual user database)
users = {
    "user1": {"password": "password1", "projects": ["Project A", "Project B"]},
    "user2": {"password": "password2", "projects": ["Project C", "Project D"]}
}

# Dummy project data (replace this with your actual project database)
projects = {
    "Project A": {"description": "Description of Project A"},
    "Project B": {"description": "Description of Project B"},
    "Project C": {"description": "Description of Project C"},
    "Project D": {"description": "Description of Project D"}
}

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    if username in users and users[username]["password"] == password:
        # Successful login
        return redirect(url_for('dashboard', username=username))
    else:
        # Failed login
        return render_template('login.html', message="Invalid username or password")

@app.route('/signup')
def signup():
    return render_template('signup.html')

@app.route('/dashboard/<username>')
def dashboard(username):
    user_projects = users[username]["projects"]
    recommended_projects = [projects[project] for project in user_projects]
    return render_template('dashboard.html', username=username, projects=recommended_projects)

if __name__ == '__main__':
    app.run(debug=True)

 '''

''' from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Dummy user data (replace this with your actual user database)
users = {
    "user1": {"password": "password1", "projects": ["Project A", "Project B"]},
    "user2": {"password": "password2", "projects": ["Project C", "Project D"]}
}

# Dummy project data (replace this with your actual project database)
projects = {
    "Project A": {"description": "Description of Project A"},
    "Project B": {"description": "Description of Project B"},
    "Project C": {"description": "Description of Project C"},
    "Project D": {"description": "Description of Project D"}
}

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    if username in users and users[username]["password"] == password:
        # Successful login
        return redirect(url_for('dashboard', username=username))
    else:
        # Failed login
        return render_template('login.html', message="Invalid username or password")

@app.route('/dashboard/<username>')
def dashboard(username):
    user_projects = users[username]["projects"]
    recommended_projects = [projects[project] for project in user_projects]
    return render_template('dashboard.html', username=username, projects=recommended_projects)

if __name__ == '__main__':
    app.run(debug=True)

 '''


''' from flask import Flask, render_template, jsonify

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
 '''