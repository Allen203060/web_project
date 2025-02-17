from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
import hashlib
import requests
import json
import jsonify


app = Flask(__name__)

# Secret key for session management
app.secret_key = 'your_secret_key'

# Database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize SQLAlchemy
db = SQLAlchemy(app)

# Create a User model for the database
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    email = db.Column(db.String(200), nullable=False)

# Initialize the database (if it doesn't exist)
with app.app_context():
    db.create_all()

# Dummy session to simulate user logged-in state (for simplicity)
logged_in = False
user_name = None

# External API URL for dashboard data
EXTERNAL_API_URL = "https://api.example.com/data"

@app.route('/')
def home():
    return redirect(url_for('dashboard'))

# Login Route (No token required)
@app.route('/login', methods=['GET', 'POST'])
def login():
    
    global logged_in, user_name
    if request.method == 'POST':
        
        username = request.form['username']
        password = request.form['password']

        # Query the database to find the user
        user = User.query.filter_by(username=username).first()

        if user and user.password == hashlib.sha256(password.encode()).hexdigest():
            logged_in = True
            user_name = username  # In practice, generate a real token
            return redirect(url_for('dashboard'))
        else:
            flash('Invalid credentials. Please try again.', 'danger')
    
    return render_template('login.html')

# Signup Route (No token required)
@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        email = request.form['email']

        # Check if the username already exists
        existing_user = User.query.filter_by(username=username).first()
        if existing_user:
            flash('Username already exists. Please choose another.', 'danger')
            return render_template('signup.html')

        # Hash the password before storing it
        hashed_password = hashlib.sha256(password.encode()).hexdigest()

        # Create a new user in the database
        new_user = User(username=username, password=hashed_password, email= email)
        db.session.add(new_user)
        db.session.commit()

        flash('Account created successfully! Please log in.', 'success')
        return redirect(url_for('login'))
    
    return render_template('signup.html')

# Dashboard Route (Requires valid token)
@app.route('/dashboard')
def dashboard():
    

    url = "https://api.themoviedb.org/3/movie/popular?language=en-US&page=1"

    headers = {
        "accept": "application/json",
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI4N2JkNmRiZjI3ODRhZGU2ZDg3MjRhZTllMGFiYzRiYSIsIm5iZiI6MTczOTcwNTI0NS42NDcsInN1YiI6IjY3YjFjYjlkOGRjZTI5ZTNmYmUwZDM5ZiIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.QhC92XWnGlz7Ep5hshSkYhsF9S_DbqKYoZPWv8HYwe4"
    }

    response = requests.get(url, headers=headers)
    
    data = (response.text)
    # try:
    #     response = requests.get()
    #     data = response.json() if response.status_code == 200 else {}
    # except requests.exceptions.RequestException as e:
    #     data = {"error": "Failed to fetch data"}

    return render_template('index.html', data=data, user_name=user_name)

# Dashboard Route (Requires valid token)
@app.route('/movies')
def movies():
    movie_id = request.args.get('id')  # Get 'id' from query parameters
    if movie_id == None:
        return redirect(url_for('dashboard'))
    
    data = getMoieDetailsByID(movie_id)
    keywoerd = getKeyWordsByUID(movie_id)
    # try:
    #     response = requests.get()
    #     data = response.json() if response.status_code == 200 else {}
    # except requests.exceptions.RequestException as e:
    #     data = {"error": "Failed to fetch data"}

    return render_template('movies.html', data= json.loads(data), )

def getMoieDetailsByID(movie_id):
    url = "https://api.themoviedb.org/3/movie/" + movie_id

    headers = {
        "accept": "application/json",
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI4N2JkNmRiZjI3ODRhZGU2ZDg3MjRhZTllMGFiYzRiYSIsIm5iZiI6MTczOTcwNTI0NS42NDcsInN1YiI6IjY3YjFjYjlkOGRjZTI5ZTNmYmUwZDM5ZiIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.QhC92XWnGlz7Ep5hshSkYhsF9S_DbqKYoZPWv8HYwe4"
    }

    response = requests.get(url, headers=headers)

    return response.text

def getKeyWordsByUID(movie_id):
    url = "https://api.themoviedb.org/3/movie/" + movie_id

    headers = {
        "accept": "application/json",
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI4N2JkNmRiZjI3ODRhZGU2ZDg3MjRhZTllMGFiYzRiYSIsIm5iZiI6MTczOTcwNTI0NS42NDcsInN1YiI6IjY3YjFjYjlkOGRjZTI5ZTNmYmUwZDM5ZiIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.QhC92XWnGlz7Ep5hshSkYhsF9S_DbqKYoZPWv8HYwe4"
    }

    response = requests.get(url, headers=headers)

    return response.text


@app.route('/more') 
def more():
    return render_template('more.html')

@app.route('/celeb') 
def celeb():
    return render_template('celeb.html')

@app.route('/api/search')
def api_search():
    query = request.args.get('q', '')
    url = f"https://api.themoviedb.org/3/search/movie?query={query}&include_adult=false&language=en-US&page=1"
    
    headers = {
        "accept": "application/json",
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI4N2JkNmRiZjI3ODRhZGU2ZDg3MjRhZTllMGFiYzRiYSIsIm5iZiI6MTczOTcwNTI0NS42NDcsInN1YiI6IjY3YjFjYjlkOGRjZTI5ZTNmYmUwZDM5ZiIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.QhC92XWnGlz7Ep5hshSkYhsF9S_DbqKYoZPWv8HYwe4"
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        return (data.get('results', []))
    return jsonify([])


@app.route('/logout')
def logout():
    global logged_in, user_name
    logged_in = False
    user_name = None
    return redirect(url_for('dashboard'))


if __name__ == '__main__':
    app.run(debug=True)
