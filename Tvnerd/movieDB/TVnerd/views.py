from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import JsonResponse
from .models import User, Movie, Comment
import hashlib, requests, json
from datetime import datetime, timedelta
from django.contrib.auth.decorators import login_required
from .models import Watchlist

def home(request):
    return redirect('dashboard')

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        remember = 'remember' in request.POST

        try:
            user = User.objects.get(username=username)
            if user.password == hashlib.sha256(password.encode()).hexdigest():
                request.session['username'] = username
                request.session['user_id'] = user.id
                request.session['login_time'] = datetime.utcnow().isoformat()
                request.session.set_expiry(2592000 if remember else 0)  # 30 days or session

                messages.success(request, 'Login successful!')
                return redirect('dashboard')
            else:
                messages.error(request, 'Invalid credentials.')
        except User.DoesNotExist:
            messages.error(request, 'User not found.')

    return render(request, 'Tvnerd/login.html')

def signup_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']

        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists. Please choose another.')
            return render(request, 'Tvnerd/signup.html')

        hashed_password = hashlib.sha256(password.encode()).hexdigest()
        new_user = User(username=username, password=hashed_password, email=email)
        new_user.save()

        messages.success(request, 'Account created successfully! Please log in.')
        return redirect('login')

    return render(request, 'Tvnerd/signup.html')

def logout_view(request):
    request.session.flush()
    messages.info(request, 'Logged out successfully.')
    return redirect('login')

def dashboard_view(request):
    if 'username' not in request.session:
        return redirect('login')

    last_login = request.session.get('login_time')
    if last_login:
        last_login = datetime.fromisoformat(last_login)
        if datetime.utcnow() - last_login > timedelta(minutes=30):
            request.session.flush()
            messages.warning(request, 'Session expired.')
            return redirect('login')

    request.session['login_time'] = datetime.utcnow().isoformat()

    url = "https://api.themoviedb.org/3/movie/popular?language=en-US&page=1"
    headers = {
        "accept": "application/json",
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI4N2JkNmRiZjI3ODRhZGU2ZDg3MjRhZTllMGFiYzRiYSIsIm5iZiI6MTczOTcwNTI0NS42NDcsInN1YiI6IjY3YjFjYjlkOGRjZTI5ZTNmYmUwZDM5ZiIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.QhC92XWnGlz7Ep5hshSkYhsF9S_DbqKYoZPWv8HYwe4"
    }
    response = requests.get(url, headers=headers)
    data = response.json() if response.status_code == 200 else {}

    return render(request, 'Tvnerd/index.html', {
        'data': data,
        'user_name': request.session.get('username'),
        'is_permanent': request.session.get_expiry_age() > 0  
    })

def get_movie_details_by_id(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}"
    headers = {
        "accept": "application/json",
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI4N2JkNmRiZjI3ODRhZGU2ZDg3MjRhZTllMGFiYzRiYSIsIm5iZiI6MTczOTcwNTI0NS42NDcsInN1YiI6IjY3YjFjYjlkOGRjZTI5ZTNmYmUwZDM5ZiIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.QhC92XWnGlz7Ep5hshSkYhsF9S_DbqKYoZPWv8HYwe4"
    }
    response = requests.get(url, headers=headers)
    return response.json() if response.status_code == 200 else {}

def api_search(request):
    query = request.GET.get('q', '')
    url = f"https://api.themoviedb.org/3/search/movie?query={query}&include_adult=false&language=en-US&page=1"
    headers = {
        "accept": "application/json",
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI4N2JkNmRiZjI3ODRhZGU2ZDg3MjRhZTllMGFiYzRiYSIsIm5iZiI6MTczOTcwNTI0NS42NDcsInN1YiI6IjY3YjFjYjlkOGRjZTI5ZTNmYmUwZDM5ZiIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.QhC92XWnGlz7Ep5hshSkYhsF9S_DbqKYoZPWv8HYwe4"
    }
    response = requests.get(url, headers=headers)
    return JsonResponse(response.json().get('results', []), safe=False) if response.status_code == 200 else JsonResponse([])



def movies_view(request):
    movie_id = request.GET.get('id')
    if not movie_id:
        return redirect('movies')  # Redirect if no ID, adjust as needed

    # Fetch movie details
    url = f'https://api.themoviedb.org/3/movie/{movie_id}?language=en-US'
    headers = {
        "accept": "application/json",
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI4N2JkNmRiZjI3ODRhZGU2ZDg3MjRhZTllMGFiYzRiYSIsIm5iZiI6MTczOTcwNTI0NS42NDcsInN1YiI6IjY3YjFjYjlkOGRjZTI5ZTNmYmUwZDM5ZiIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.QhC92XWnGlz7Ep5hshSkYhsF9S_DbqKYoZPWv8HYwe4"
    }
    movie_response = requests.get(url, headers=headers)
    data = movie_response.json() if movie_response.status_code == 200 else {}

    # Fetch credits
    credits_url = f'https://api.themoviedb.org/3/movie/{movie_id}/credits?language=en-US'
    credits_response = requests.get(credits_url, headers=headers)
    credits_data = credits_response.json() if credits_response.status_code == 200 else {'cast': [], 'crew': []}
    data['credits'] = credits_data

    # Fetch reviews
    reviews_url = f'https://api.themoviedb.org/3/movie/{movie_id}/reviews?language=en-US'
    reviews_response = requests.get(reviews_url, headers=headers)
    reviews_data = reviews_response.json() if reviews_response.status_code == 200 else {'results': []}
    data['reviews'] = reviews_data

    # Get or create movie in database
    movie, created = Movie.objects.get_or_create(
        tmdb_id=movie_id,
        defaults={
            'title': data.get('title', ''),
            'poster_path': data.get('poster_path', ''),
            'overview': data.get('overview', '')
        }
    )

    # Fetch comments
    comments = movie.comments.all().order_by('-created_at')

    # Handle comment submission
    if request.method == 'POST' and request.session.get('username'):
        content = request.POST.get('content')
        if content:
            user = User.objects.get(username=request.session['username'])
            Comment.objects.create(
                user=user,
                movie=movie,
                content=content
            )
            return redirect(f'/movies/?id={movie_id}')

    return render(request, 'Tvnerd/movies.html', {
        'data': data,
        'comments': comments,
    })


def watchlist_view(request):
    if 'username' not in request.session:
        return redirect('login')

    user = User.objects.get(username=request.session['username'])
    watchlist = Watchlist.objects.filter(user=user)

    return render(request, 'Tvnerd/watchlist.html', {'watchlist': watchlist})

def add_to_watchlist(request):
    if request.method == 'POST' and 'user_id' in request.session:
        user_id = request.session['user_id']
        movie_id = request.POST.get('movie_id')
        title = request.POST.get('title')
        poster_path = request.POST.get('poster_path')

        # Prevent duplicates
        if not Watchlist.objects.filter(user_id=user_id, movie_id=movie_id).exists():
            Watchlist.objects.create(
                user_id=user_id,
                movie_id=movie_id,
                title=title,
                poster_path=poster_path
            )
            messages.success(request, f'"{title}" added to your watchlist.')
        else:
            messages.info(request, f'"{title}" is already in your watchlist.')

    return redirect(f"/movies/?id={movie_id}")

def remove_from_watchlist(request, movie_id):
    if 'user_id' not in request.session:
        return redirect('login')

    user_id = request.session['user_id']
    Watchlist.objects.filter(user_id=user_id, movie_id=movie_id).delete()
    messages.success(request, 'Movie removed from watchlist.')
    return redirect('watchlist')

def news(request):
    return render(request, 'Tvnerd/news.html')

def nominees(request):
    return render(request, 'Tvnerd/nominees.html')

def more(request):
    return render(request, 'Tvnerd/awards.html')

def celeb(request):
    return render(request, 'Tvnerd/celeb.html')

def tvshow(request):
    return render(request, 'Tvnerd/tvshow.html')