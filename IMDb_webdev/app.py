from flask import Flask, render_template, request, redirect, url_for, flash, session, jsonify
from flask_sqlalchemy import SQLAlchemy
import hashlib
import requests
import json
import logging
from datetime import timedelta, datetime

# Configure logging
logging.basicConfig(level=logging.DEBUG)

app = Flask(__name__)

# Secret key for session management
app.secret_key = 'your_secret_key'

# Database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(days=30)

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

@app.route('/')
def home():
    return redirect(url_for('dashboard'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        remember = 'remember' in request.form

        user = User.query.filter_by(username=username).first()

        if user and user.password == hashlib.sha256(password.encode()).hexdigest():
            session['username'] = username
            session['user_id'] = user.id
            session['login_time'] = datetime.utcnow().isoformat()
            session.permanent = remember

            flash('Login successful!', 'success')
            return redirect(url_for('dashboard'))
        else:
            flash('Invalid credentials. Please try again.', 'danger')

    return render_template('login.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        email = request.form['email']

        logging.debug(f"Received form data: username={username}, email={email}")

        if User.query.filter_by(username=username).first():
            flash('Username already exists. Please choose another.', 'danger')
            return render_template('signup.html')

        hashed_password = hashlib.sha256(password.encode()).hexdigest()
        new_user = User(username=username, password=hashed_password, email=email)
        db.session.add(new_user)
        db.session.commit()

        flash('Account created successfully! Please log in.', 'success')
        return redirect(url_for('login'))
    
    return render_template('signup.html')

@app.route('/logout', methods=['POST', 'GET'])
def logout():
    session.clear()
    flash('Logged out successfully.', 'info')
    return redirect(url_for('login'))

@app.before_request
def check_session_expiry():
    if 'username' in session and 'login_time' in session:
        last_activity = datetime.fromisoformat(session['login_time'])
        if datetime.utcnow() - last_activity > timedelta(minutes=30):
            session.clear()
            flash('Session expired due to inactivity.', 'warning')
            return redirect(url_for('login'))
    session['login_time'] = datetime.utcnow().isoformat()

@app.route('/dashboard')
def dashboard():
    if 'username' not in session:
        return redirect(url_for('login'))
    
    url = "https://api.themoviedb.org/3/movie/popular?language=en-US&page=1"
    headers = {"accept": "application/json", "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI4N2JkNmRiZjI3ODRhZGU2ZDg3MjRhZTllMGFiYzRiYSIsIm5iZiI6MTczOTcwNTI0NS42NDcsInN1YiI6IjY3YjFjYjlkOGRjZTI5ZTNmYmUwZDM5ZiIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.QhC92XWnGlz7Ep5hshSkYhsF9S_DbqKYoZPWv8HYwe4"
    }
    response = requests.get(url, headers=headers)
    data = response.json() if response.status_code == 200 else {}

    return render_template('index.html', data=data, user_name=session['username'])

@app.route('/movies')
def movies():
    movie_id = request.args.get('id')
    if not movie_id:
        return redirect(url_for('dashboard'))
    
    data = get_movie_details_by_id(movie_id)
    return render_template('movies.html', data=json.loads(data))

def get_movie_details_by_id(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}"
    headers = {"accept": "application/json", "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI4N2JkNmRiZjI3ODRhZGU2ZDg3MjRhZTllMGFiYzRiYSIsIm5iZiI6MTczOTcwNTI0NS42NDcsInN1YiI6IjY3YjFjYjlkOGRjZTI5ZTNmYmUwZDM5ZiIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.QhC92XWnGlz7Ep5hshSkYhsF9S_DbqKYoZPWv8HYwe4"
    }
    response = requests.get(url, headers=headers)
    return response.text

@app.route('/api/search')
def api_search():
    query = request.args.get('q', '')
    url = f"https://api.themoviedb.org/3/search/movie?query={query}&include_adult=false&language=en-US&page=1"
    headers = {"accept": "application/json", "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI4N2JkNmRiZjI3ODRhZGU2ZDg3MjRhZTllMGFiYzRiYSIsIm5iZiI6MTczOTcwNTI0NS42NDcsInN1YiI6IjY3YjFjYjlkOGRjZTI5ZTNmYmUwZDM5ZiIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.QhC92XWnGlz7Ep5hshSkYhsF9S_DbqKYoZPWv8HYwe4"
    }
    response = requests.get(url, headers=headers)
    return jsonify(response.json().get('results', [])) if response.status_code == 200 else jsonify([])

if __name__ == '__main__':
    app.run(debug=True)
