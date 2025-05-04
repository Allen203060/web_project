# from django.shortcuts import render, redirect
# from django.contrib import messages
# from django.http import JsonResponse
# from .models import User, Movie, Comment
# import hashlib, requests, json
# from datetime import datetime, timedelta
# from django.contrib.auth.decorators import login_required
# from .models import Watchlist

# def home(request):
#     return redirect('dashboard')

# def login_view(request):
#     if request.method == 'POST':
#         username = request.POST['username']
#         password = request.POST['password']
#         remember = 'remember' in request.POST

#         try:
#             user = User.objects.get(username=username)
#             if user.password == hashlib.sha256(password.encode()).hexdigest():
#                 request.session['username'] = username
#                 request.session['user_id'] = user.id
#                 request.session['login_time'] = datetime.utcnow().isoformat()
#                 request.session.set_expiry(2592000 if remember else 0)  # 30 days or session

#                 messages.success(request, 'Login successful!')
#                 return redirect('dashboard')
#             else:
#                 messages.error(request, 'Invalid credentials.')
#         except User.DoesNotExist:
#             messages.error(request, 'User not found.')

#     return render(request, 'Tvnerd/login.html')

# def signup_view(request):
#     if request.method == 'POST':
#         username = request.POST['username']
#         password = request.POST['password']
#         email = request.POST['email']

#         if User.objects.filter(username=username).exists():
#             messages.error(request, 'Username already exists. Please choose another.')
#             return render(request, 'Tvnerd/signup.html')

#         hashed_password = hashlib.sha256(password.encode()).hexdigest()
#         new_user = User(username=username, password=hashed_password, email=email)
#         new_user.save()

#         messages.success(request, 'Account created successfully! Please log in.')
#         return redirect('login')

#     return render(request, 'Tvnerd/signup.html')

# def logout_view(request):
#     request.session.flush()
#     messages.info(request, 'Logged out successfully.')
#     return redirect('login')

# def dashboard_view(request):
#     if 'username' not in request.session:
#         return redirect('login')

#     # ... session checks ...

#     # Fetch "Now Playing" (latest) movies from TMDb
#     now_playing_url = "https://api.themoviedb.org/3/movie/now_playing?language=en-US&page=1"

#     trending_url = "https://api.themoviedb.org/3/trending/movie/week?language=en-US"
#     headers = {
#         "accept": "application/json",
#         "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI4N2JkNmRiZjI3ODRhZGU2ZDg3MjRhZTllMGFiYzRiYSIsIm5iZiI6MTczOTcwNTI0NS42NDcsInN1YiI6IjY3YjFjYjlkOGRjZTI5ZTNmYmUwZDM5ZiIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.QhC92XWnGlz7Ep5hshSkYhsF9S_DbqKYoZPWv8HYwe4"
#     }
#     now_playing_response = requests.get(now_playing_url, headers=headers)
#     now_playing = now_playing_response.json().get('results', []) if now_playing_response.status_code == 200 else []

#     trending_response = requests.get(trending_url, headers=headers)
#     top_movies = trending_response.json().get('results', [])[:10] if trending_response.status_code == 200 else []

#     return render(request, 'Tvnerd/index.html', {
#         'latest_movies': now_playing,
#         'top_movies': top_movies,
#         'user_name': request.session.get('username'),
#         'is_permanent': request.session.get_expiry_age() > 0
#     })

# def tvshow(request):
#     # Fetch latest TV shows
#     latest_url = "https://api.themoviedb.org/3/tv/latest?language=en-US"
#     popular_url = "https://api.themoviedb.org/3/tv/popular?language=en-US"
    
#     headers = {
#         "accept": "application/json",
#         "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI4N2JkNmRiZjI3ODRhZGU2ZDg3MjRhZTllMGFiYzRiYSIsIm5iZiI6MTczOTcwNTI0NS42NDcsInN1YiI6IjY3YjFjYjlkOGRjZTI5ZTNmYmUwZDM5ZiIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.QhC92XWnGlz7Ep5hshSkYhsF9S_DbqKYoZPWv8HYwe4"   
#     }

#     try:
#         # Fetch latest TV shows
#         latest_response = requests.get(latest_url, headers=headers)
#         latest_shows = latest_response.json().get('results', [])[:8] if latest_response.status_code == 200 else []
        
#         # Fetch popular TV shows
#         popular_response = requests.get(popular_url, headers=headers)
#         popular_shows = popular_response.json().get('results', [])[:10] if popular_response.status_code == 200 else []

#     except requests.exceptions.RequestException as e:
#         latest_shows = []
#         popular_shows = []

#     return render(request, 'Tvnerd/tvshow.html', {
#         'latest_tv_shows': latest_shows,
#         'popular_tv_shows': popular_shows
#     })


# def api_search(request):
#     query = request.GET.get('q', '')
#     url = f"https://api.themoviedb.org/3/search/movie?query={query}&include_adult=false&language=en-US&page=1"
#     headers = {
#         "accept": "application/json",
#         "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI4N2JkNmRiZjI3ODRhZGU2ZDg3MjRhZTllMGFiYzRiYSIsIm5iZiI6MTczOTcwNTI0NS42NDcsInN1YiI6IjY3YjFjYjlkOGRjZTI5ZTNmYmUwZDM5ZiIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.QhC92XWnGlz7Ep5hshSkYhsF9S_DbqKYoZPWv8HYwe4"
#     }
#     response = requests.get(url, headers=headers)
#     return JsonResponse(response.json().get('results', []), safe=False) if response.status_code == 200 else JsonResponse([])



# def movies_view(request):
#     movie_id = request.GET.get('id')
#     if not movie_id:
#         return redirect('movies')  # Redirect if no ID, adjust as needed

#     # Fetch movie details
#     url = f'https://api.themoviedb.org/3/movie/{movie_id}?language=en-US'
#     headers = {
#         "accept": "application/json",
#         "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI4N2JkNmRiZjI3ODRhZGU2ZDg3MjRhZTllMGFiYzRiYSIsIm5iZiI6MTczOTcwNTI0NS42NDcsInN1YiI6IjY3YjFjYjlkOGRjZTI5ZTNmYmUwZDM5ZiIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.QhC92XWnGlz7Ep5hshSkYhsF9S_DbqKYoZPWv8HYwe4"
#     }
#     movie_response = requests.get(url, headers=headers)
#     data = movie_response.json() if movie_response.status_code == 200 else {}

#     # Fetch credits
#     credits_url = f'https://api.themoviedb.org/3/movie/{movie_id}/credits?language=en-US'
#     credits_response = requests.get(credits_url, headers=headers)
#     credits_data = credits_response.json() if credits_response.status_code == 200 else {'cast': [], 'crew': []}
#     data['credits'] = credits_data

#     # Fetch reviews
#     reviews_url = f'https://api.themoviedb.org/3/movie/{movie_id}/reviews?language=en-US'
#     reviews_response = requests.get(reviews_url, headers=headers)
#     reviews_data = reviews_response.json() if reviews_response.status_code == 200 else {'results': []}
#     data['reviews'] = reviews_data

#     # Get or create movie in database
#     movie, created = Movie.objects.get_or_create(
#         tmdb_id=movie_id,
#         defaults={
#             'title': data.get('title', ''),
#             'poster_path': data.get('poster_path', ''),
#             'overview': data.get('overview', '')
#         }
#     )

#     # Fetch comments
#     comments = movie.comments.all().order_by('-created_at')

#     # Handle comment submission
#     if request.method == 'POST' and request.session.get('username'):
#         content = request.POST.get('content')
#         if content:
#             user = User.objects.get(username=request.session['username'])
#             Comment.objects.create(
#                 user=user,
#                 movie=movie,
#                 content=content
#             )
#             return redirect(f'/movies/?id={movie_id}')

#     return render(request, 'Tvnerd/movies.html', {
#         'data': data,
#         'comments': comments,
#     })

# def tvshow_detail(request):
#     tv_id = request.GET.get('id')
#     if not tv_id:
#         return redirect('tvshows')
    
#     # Fetch TV show details
#     url = f'https://api.themoviedb.org/3/tv/{tv_id}?language=en-US'
#     headers = {
#         "accept": "application/json",
#         "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI4N2JkNmRiZjI3ODRhZGU2ZDg3MjRhZTllMGFiYzRiYSIsIm5iZiI6MTczOTcwNTI0NS42NDcsInN1YiI6IjY3YjFjYjlkOGRjZTI5ZTNmYmUwZDM5ZiIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.QhC92XWnGlz7Ep5hshSkYhsF9S_DbqKYoZPWv8HYwe4"
#     }
    
#     response = requests.get(url, headers=headers)
#     data = response.json() if response.status_code == 200 else {}
    
#     # Fetch credits
#     credits_url = f'https://api.themoviedb.org/3/tv/{tv_id}/credits?language=en-US'
#     credits_response = requests.get(credits_url, headers=headers)
#     data['credits'] = credits_response.json() if credits_response.status_code == 200 else {'cast': [], 'crew': []}
    
#     # Fetch reviews
#     reviews_url = f'https://api.themoviedb.org/3/tv/{tv_id}/reviews?language=en-US'
#     reviews_response = requests.get(reviews_url, headers=headers)
#     data['reviews'] = reviews_response.json() if reviews_response.status_code == 200 else {'results': []}
    
#     return render(request, 'Tvnerd/shows.html', {
#         'data': data,
#         # Add comment handling similar to movies_view if needed
#     })


# def api_search_tv(request):
#     query = request.GET.get('q', '')
#     url = f"https://api.themoviedb.org/3/search/tv?query={query}&language=en-US&page=1"
#     headers = {
#         "accept": "application/json",
#         "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI4N2JkNmRiZjI3ODRhZGU2ZDg3MjRhZTllMGFiYzRiYSIsIm5iZiI6MTczOTcwNTI0NS42NDcsInN1YiI6IjY3YjFjYjlkOGRjZTI5ZTNmYmUwZDM5ZiIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.QhC92XWnGlz7Ep5hshSkYhsF9S_DbqKYoZPWv8HYwe4"
#     }
#     response = requests.get(url, headers=headers)
#     return JsonResponse(response.json().get('results', []), safe=False) if response.status_code == 200 else JsonResponse([], safe=False)


# def watchlist_view(request):
#     if 'username' not in request.session:
#         return redirect('login')

#     user = User.objects.get(username=request.session['username'])
#     watchlist = Watchlist.objects.filter(user=user)

#     return render(request, 'Tvnerd/watchlist.html', {'watchlist': watchlist})

# def add_to_watchlist(request):
#     if request.method == 'POST' and 'user_id' in request.session:
#         user_id = request.session['user_id']
#         movie_id = request.POST.get('movie_id')
#         title = request.POST.get('title')
#         poster_path = request.POST.get('poster_path')

#         # Prevent duplicates
#         if not Watchlist.objects.filter(user_id=user_id, movie_id=movie_id).exists():
#             Watchlist.objects.create(
#                 user_id=user_id,
#                 movie_id=movie_id,
#                 title=title,
#                 poster_path=poster_path
#             )
#             messages.success(request, f'"{title}" added to your watchlist.')
#         else:
#             messages.info(request, f'"{title}" is already in your watchlist.')

#     return redirect(f"/movies/?id={movie_id}")

# def remove_from_watchlist(request, movie_id):
#     if 'user_id' not in request.session:
#         return redirect('login')

#     user_id = request.session['user_id']
#     Watchlist.objects.filter(user_id=user_id, movie_id=movie_id).delete()
#     messages.success(request, 'Movie removed from watchlist.')
#     return redirect('watchlist')

# def news(request):
#     return render(request, 'Tvnerd/news.html')

# def nominees(request):
#     return render(request, 'Tvnerd/nominees.html')

# def video(request):
#     return render(request, 'Tvnerd/video.html')

# def more(request):
#     return render(request, 'Tvnerd/awards.html')

# def celeb(request):
#     return render(request, 'Tvnerd/celeb.html')


# from django.shortcuts import render, redirect
# from django.contrib import messages
# from django.http import JsonResponse
# from .models import User, Movie, Comment, Watchlist, Notification
# import hashlib, requests, json
# from datetime import datetime, timedelta
# import requests as api_requests

# def home(request):
#     return redirect('dashboard')

# def login_view(request):
#     if request.method == 'POST':
#         username = request.POST['username']
#         password = request.POST['password']
#         remember = 'remember' in request.POST

#         try:
#             user = User.objects.get(username=username)
#             if user.password == hashlib.sha256(password.encode()).hexdigest():
#                 request.session['username'] = username
#                 request.session['user_id'] = user.id
#                 request.session['login_time'] = datetime.utcnow().isoformat()
#                 request.session.set_expiry(2592000 if remember else 0)  # 30 days or session

#                 messages.success(request, 'Login successful!')
#                 return redirect('dashboard')
#             else:
#                 messages.error(request, 'Invalid credentials.')
#         except User.DoesNotExist:
#             messages.error(request, 'User not found.')

#     return render(request, 'Tvnerd/login.html')

# def signup_view(request):
#     if request.method == 'POST':
#         username = request.POST['username']
#         password = request.POST['password']
#         email = request.POST['email']

#         if User.objects.filter(username=username).exists():
#             messages.error(request, 'Username already exists. Please choose another.')
#             return render(request, 'Tvnerd/signup.html')

#         hashed_password = hashlib.sha256(password.encode()).hexdigest()
#         new_user = User(username=username, password=hashed_password, email=email)
#         new_user.save()

#         messages.success(request, 'Account created successfully! Please log in.')
#         return redirect('login')

#     return render(request, 'Tvnerd/signup.html')

# def logout_view(request):
#     request.session.flush()
#     messages.info(request, 'Logged out successfully.')
#     return redirect('login')

# def dashboard_view(request):
#     if 'username' not in request.session:
#         return redirect('login')

#     # Fetch "Now Playing" (latest) movies from TMDb
#     now_playing_url = "https://api.themoviedb.org/3/movie/now_playing?language=en-US&page=1"
#     trending_url = "https://api.themoviedb.org/3/trending/movie/week?language=en-US"
#     headers = {
#         "accept": "application/json",
#         "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI4N2JkNmRiZjI3ODRhZGU2ZDg3MjRhZTllMGFiYzRiYSIsIm5iZiI6MTczOTcwNTI0NS42NDcsInN1YiI6IjY3YjFjYjlkOGRjZTI5ZTNmYmUwZDM5ZiIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.QhC92XWnGlz7Ep5hshSkYhsF9S_DbqKYoZPWv8HYwe4"
#     }
#     now_playing_response = api_requests.get(now_playing_url, headers=headers)
#     now_playing = now_playing_response.json().get('results', []) if now_playing_response.status_code == 200 else []

#     trending_response = api_requests.get(trending_url, headers=headers)
#     top_movies = trending_response.json().get('results', [])[:10] if trending_response.status_code == 200 else []

#     # Fetch featured movies from the database
#     featured_movies = Movie.objects.filter(is_featured=True)

#     return render(request, 'Tvnerd/index.html', {
#         'latest_movies': now_playing,
#         'top_movies': top_movies,
#         'featured_movies': featured_movies,
#         'user_name': request.session.get('username'),
#         'is_permanent': request.session.get_expiry_age() > 0
#     })

# def tvshow(request):
#     latest_url = "https://api.themoviedb.org/3/tv/latest?language=en-US"
#     popular_url = "https://api.themoviedb.org/3/tv/popular?language=en-US"
#     headers = {
#         "accept": "application/json",
#         "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI4N2JkNmRiZjI3ODRhZGU2ZDg3MjRhZTllMGFiYzRiYSIsIm5iZiI6MTczOTcwNTI0NS42NDcsInN1YiI6IjY3YjFjYjlkOGRjZTI5ZTNmYmUwZDM5ZiIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.QhC92XWnGlz7Ep5hshSkYhsF9S_DbqKYoZPWv8HYwe4"   
#     }

#     try:
#         latest_response = api_requests.get(latest_url, headers=headers)
#         latest_shows = latest_response.json().get('results', [])[:8] if latest_response.status_code == 200 else []
#         popular_response = api_requests.get(popular_url, headers=headers)
#         popular_shows = popular_response.json().get('results', [])[:10] if popular_response.status_code == 200 else []
#     except api_requests.exceptions.RequestException as e:
#         latest_shows = []
#         popular_shows = []

#     return render(request, 'Tvnerd/tvshow.html', {
#         'latest_tv_shows': latest_shows,
#         'popular_tv_shows': popular_shows
#     })

# def api_search(request):
#     query = request.GET.get('q', '')
#     url = f"https://api.themoviedb.org/3/search/movie?query={query}&include_adult=false&language=en-US&page=1"
#     headers = {
#         "accept": "application/json",
#         "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI4N2JkNmRiZjI3ODRhZGU2ZDg3MjRhZTllMGFiYzRiYSIsIm5iZiI6MTczOTcwNTI0NS42NDcsInN1YiI6IjY3YjFjYjlkOGRjZTI5ZTNmYmUwZDM5ZiIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.QhC92XWnGlz7Ep5hshSkYhsF9S_DbqKYoZPWv8HYwe4"
#     }
#     response = api_requests.get(url, headers=headers)
#     return JsonResponse(response.json().get('results', []), safe=False) if response.status_code == 200 else JsonResponse([])

# def movies_view(request):
#     movie_id = request.GET.get('id')
#     if not movie_id:
#         return redirect('movies')

#     url = f'https://api.themoviedb.org/3/movie/{movie_id}?language=en-US'
#     headers = {
#         "accept": "application/json",
#         "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI4N2JkNmRiZjI3ODRhZGU2ZDg3MjRhZTllMGFiYzRiYSIsIm5iZiI6MTczOTcwNTI0NS42NDcsInN1YiI6IjY3YjFjYjlkOGRjZTI5ZTNmYmUwZDM5ZiIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.QhC92XWnGlz7Ep5hshSkYhsF9S_DbqKYoZPWv8HYwe4"
#     }
#     movie_response = api_requests.get(url, headers=headers)
#     data = movie_response.json() if movie_response.status_code == 200 else {}

#     credits_url = f'https://api.themoviedb.org/3/movie/{movie_id}/credits?language=en-US'
#     credits_response = api_requests.get(credits_url, headers=headers)
#     credits_data = credits_response.json() if credits_response.status_code == 200 else {'cast': [], 'crew': []}
#     data['credits'] = credits_data

#     reviews_url = f'https://api.themoviedb.org/3/movie/{movie_id}/reviews?language=en-US'
#     reviews_response = api_requests.get(reviews_url, headers=headers)
#     reviews_data = reviews_response.json() if reviews_response.status_code == 200 else {'results': []}
#     data['reviews'] = reviews_data

#     movie, created = Movie.objects.get_or_create(
#         tmdb_id=movie_id,
#         defaults={
#             'title': data.get('title', ''),
#             'poster_path': data.get('poster_path', ''),
#             'overview': data.get('overview', '')
#         }
#     )

#     comments = movie.comments.all().order_by('-created_at')

#     if request.method == 'POST' and request.session.get('username'):
#         content = request.POST.get('content')
#         if content:
#             user = User.objects.get(username=request.session['username'])
#             comment = Comment.objects.create(
#                 user=user,
#                 movie=movie,
#                 content=content
#             )
#             # Notify users who have this movie in their watchlist or commented on it
#             watchlist_users = Watchlist.objects.filter(movie_id=movie_id).values_list('user', flat=True)
#             commented_users = Comment.objects.filter(movie=movie).values_list('user', flat=True)
#             notify_users = set(watchlist_users) | set(commented_users) - {user.id}  # Exclude the commenter
#             for user_id in notify_users:
#                 notification_data = {
#                     'user_id': user_id,
#                     'message': f"New comment on '{movie.title}' by {user.username}",
#                     'related_movie_id': movie.id
#                 }
#                 api_response = api_requests.post('http://localhost:5000/api/notifications', json=notification_data)
#                 if api_response.status_code != 201:
#                     messages.error(request, 'Failed to create notification.')
#             return redirect(f'/movies/?id={movie_id}')

#     return render(request, 'Tvnerd/movies.html', {
#         'data': data,
#         'comments': comments,
#     })

# def tvshow_detail(request):
#     tv_id = request.GET.get('id')
#     if not tv_id:
#         return redirect('tvshows')
    
#     url = f'https://api.themoviedb.org/3/tv/{tv_id}?language=en-US'
#     headers = {
#         "accept": "application/json",
#         "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI4N2JkNmRiZjI3ODRhZGU2ZDg3MjRhZTllMGFiYzRiYSIsIm5iZiI6MTczOTcwNTI0NS42NDcsInN1YiI6IjY3YjFjYjlkOGRjZTI5ZTNmYmUwZDM5ZiIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.QhC92XWnGlz7Ep5hshSkYhsF9S_DbqKYoZPWv8HYwe4"
#     }
    
#     response = api_requests.get(url, headers=headers)
#     data = response.json() if response.status_code == 200 else {}
    
#     credits_url = f'https://api.themoviedb.org/3/tv/{tv_id}/credits?language=en-US'
#     credits_response = api_requests.get(credits_url, headers=headers)
#     data['credits'] = credits_response.json() if credits_response.status_code == 200 else {'cast': [], 'crew': []}
    
#     reviews_url = f'https://api.themoviedb.org/3/tv/{tv_id}/reviews?language=en-US'
#     reviews_response = api_requests.get(reviews_url, headers=headers)
#     data['reviews'] = reviews_response.json() if reviews_response.status_code == 200 else {'results': []}
    
#     return render(request, 'Tvnerd/shows.html', {
#         'data': data,
#     })

# def api_search_tv(request):
#     query = request.GET.get('q', '')
#     url = f"https://api.themoviedb.org/3/search/tv?query={query}&language=en-US&page=1"
#     headers = {
#         "accept": "application/json",
#         "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI4N2JkNmRiZjI3ODRhZGU2ZDg3MjRhZTllMGFiYzRiYSIsIm5iZiI6MTczOTcwNTI0NS42NDcsInN1YiI6IjY3YjFjYjlkOGRjZTI5ZTNmYmUwZDM5ZiIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.QhC92XWnGlz7Ep5hshSkYhsF9S_DbqKYoZPWv8HYwe4"
#     }
#     response = api_requests.get(url, headers=headers)
#     return JsonResponse(response.json().get('results', []), safe=False) if response.status_code == 200 else JsonResponse([], safe=False)

# def watchlist_view(request):
#     if 'username' not in request.session:
#         return redirect('login')

#     user = User.objects.get(username=request.session['username'])
#     watchlist = Watchlist.objects.filter(user=user)

#     return render(request, 'Tvnerd/watchlist.html', {'watchlist': watchlist})

# def add_to_watchlist(request):
#     if request.method == 'POST' and 'user_id' in request.session:
#         user_id = request.session['user_id']
#         movie_id = request.POST.get('movie_id')
#         title = request.POST.get('title')
#         poster_path = request.POST.get('poster_path')

#         if not Watchlist.objects.filter(user_id=user_id, movie_id=movie_id).exists():
#             Watchlist.objects.create(
#                 user_id=user_id,
#                 movie_id=movie_id,
#                 title=title,
#                 poster_path=poster_path
#             )
#             # Create notification via Flask API
#             notification_data = {
#                 'user_id': user_id,
#                 'message': f"'{title}' added to your watchlist",
#                 'related_movie_id': Movie.objects.filter(tmdb_id=movie_id).first().id if Movie.objects.filter(tmdb_id=movie_id).exists() else None
#             }
#             api_response = api_requests.post('http://localhost:5000/api/notifications', json=notification_data)
#             if api_response.status_code == 201:
#                 messages.success(request, f'"{title}" added to your watchlist.')
#             else:
#                 messages.error(request, 'Failed to create notification.')
#         else:
#             messages.info(request, f'"{title}" is already in your watchlist.')

#     return redirect(f"/movies/?id={movie_id}")

# def remove_from_watchlist(request, movie_id):
#     if 'user_id' not in request.session:
#         return redirect('login')

#     user_id = request.session['user_id']
#     watchlist_item = Watchlist.objects.filter(user_id=user_id, movie_id=movie_id).first()
#     if watchlist_item:
#         title = watchlist_item.title
#         watchlist_item.delete()
#         # Create notification via Flask API
#         notification_data = {
#             'user_id': user_id,
#             'message': f"'{title}' removed from your watchlist",
#             'related_movie_id': Movie.objects.filter(tmdb_id=movie_id).first().id if Movie.objects.filter(tmdb_id=movie_id).exists() else None
#         }
#         api_response = api_requests.post('http://localhost:5000/api/notifications', json=notification_data)
#         if api_response.status_code == 201:
#             messages.success(request, 'Movie removed from watchlist.')
#         else:
#             messages.error(request, 'Failed to create notification.')
#     return redirect('watchlist')

# def news(request):
#     return render(request, 'Tvnerd/news.html')

# def nominees(request):
#     return render(request, 'Tvnerd/nominees.html')

# def video(request):
#     return render(request, 'Tvnerd/video.html')

# def more(request):
#     return render(request, 'Tvnerd/awards.html')

# def celeb(request):
#     return render(request, 'Tvnerd/celeb.html')

from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import JsonResponse
from .models import User, Movie, Comment, Watchlist, Notification
import hashlib, requests, json
from datetime import datetime, timedelta
import requests as api_requests

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

    return render(request, 'login.html')  # Updated from Tvnerd/login.html

def signup_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']

        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists. Please choose another.')
            return render(request, 'signup.html')  # Updated from Tvnerd/signup.html

        hashed_password = hashlib.sha256(password.encode()).hexdigest()
        new_user = User(username=username, password=hashed_password, email=email)
        new_user.save()

        messages.success(request, 'Account created successfully! Please log in.')
        return redirect('login')

    return render(request, 'signup.html')  # Updated from Tvnerd/signup.html

def logout_view(request):
    request.session.flush()
    messages.info(request, 'Logged out successfully.')
    return redirect('login')

def dashboard_view(request):
    if 'username' not in request.session:
        return redirect('login')

    # Fetch "Now Playing" (latest) movies from TMDb
    now_playing_url = "https://api.themoviedb.org/3/movie/now_playing?language=en-US&page=1"
    trending_url = "https://api.themoviedb.org/3/trending/movie/week?language=en-US"
    headers = {
        "accept": "application/json",
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI4N2JkNmRiZjI3ODRhZGU2ZDg3MjRhZTllMGFiYzRiYSIsIm5iZiI6MTczOTcwNTI0NS42NDcsInN1YiI6IjY3YjFjYjlkOGRjZTI5ZTNmYmUwZDM5ZiIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.QhC92XWnGlz7Ep5hshSkYhsF9S_DbqKYoZPWv8HYwe4"
    }
    now_playing_response = api_requests.get(now_playing_url, headers=headers)
    now_playing = now_playing_response.json().get('results', []) if now_playing_response.status_code == 200 else []

    trending_response = api_requests.get(trending_url, headers=headers)
    top_movies = trending_response.json().get('results', [])[:10] if trending_response.status_code == 200 else []

    # Fetch featured movies from the database
    featured_movies = Movie.objects.filter(is_featured=True)

    return render(request, 'index.html', {  # Updated from Tvnerd/index.html
        'latest_movies': now_playing,
        'top_movies': top_movies,
        'featured_movies': featured_movies,
        'user_name': request.session.get('username'),
        'is_permanent': request.session.get_expiry_age() > 0
    })

def tvshow(request):
    latest_url = "https://api.themoviedb.org/3/tv/latest?language=en-US"
    popular_url = "https://api.themoviedb.org/3/tv/popular?language=en-US"
    headers = {
        "accept": "application/json",
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI4N2JkNmRiZjI3ODRhZGU2ZDg3MjRhZTllMGFiYzRiYSIsIm5iZiI6MTczOTcwNTI0NS42NDcsInN1YiI6IjY3YjFjYjlkOGRjZTI5ZTNmYmUwZDM5ZiIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.QhC92XWnGlz7Ep5hshSkYhsF9S_DbqKYoZPWv8HYwe4"   
    }

    try:
        latest_response = api_requests.get(latest_url, headers=headers)
        latest_shows = latest_response.json().get('results', [])[:8] if latest_response.status_code == 200 else []
        popular_response = api_requests.get(popular_url, headers=headers)
        popular_shows = popular_response.json().get('results', [])[:10] if popular_response.status_code == 200 else []
    except api_requests.exceptions.RequestException as e:
        latest_shows = []
        popular_shows = []

    return render(request, 'tvshow.html', {  # Updated from Tvnerd/tvshow.html
        'latest_tv_shows': latest_shows,
        'popular_tv_shows': popular_shows
    })

def api_search(request):
    query = request.GET.get('q', '')
    url = f"https://api.themoviedb.org/3/search/movie?query={query}&include_adult=false&language=en-US&page=1"
    headers = {
        "accept": "application/json",
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI4N2JkNmRiZjI3ODRhZGU2ZDg3MjRhZTllMGFiYzRiYSIsIm5iZiI6MTczOTcwNTI0NS42NDcsInN1YiI6IjY3YjFjYjlkOGRjZTI5ZTNmYmUwZDM5ZiIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.QhC92XWnGlz7Ep5hshSkYhsF9S_DbqKYoZPWv8HYwe4"
    }
    response = api_requests.get(url, headers=headers)
    return JsonResponse(response.json().get('results', []), safe=False) if response.status_code == 200 else JsonResponse([])

def movies_view(request):
    movie_id = request.GET.get('id')
    if not movie_id:
        return redirect('movies')

    url = f'https://api.themoviedb.org/3/movie/{movie_id}?language=en-US'
    headers = {
        "accept": "application/json",
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI4N2JkNmRiZjI3ODRhZGU2ZDg3MjRhZTllMGFiYzRiYSIsIm5iZiI6MTczOTcwNTI0NS42NDcsInN1YiI6IjY3YjFjYjlkOGRjZTI5ZTNmYmUwZDM5ZiIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.QhC92XWnGlz7Ep5hshSkYhsF9S_DbqKYoZPWv8HYwe4"
    }
    movie_response = api_requests.get(url, headers=headers)
    data = movie_response.json() if movie_response.status_code == 200 else {}

    credits_url = f'https://api.themoviedb.org/3/movie/{movie_id}/credits?language=en-US'
    credits_response = api_requests.get(credits_url, headers=headers)
    credits_data = credits_response.json() if credits_response.status_code == 200 else {'cast': [], 'crew': []}
    data['credits'] = credits_data

    reviews_url = f'https://api.themoviedb.org/3/movie/{movie_id}/reviews?language=en-US'
    reviews_response = api_requests.get(reviews_url, headers=headers)
    reviews_data = reviews_response.json() if reviews_response.status_code == 200 else {'results': []}
    data['reviews'] = reviews_data

    movie, created = Movie.objects.get_or_create(
        tmdb_id=movie_id,
        defaults={
            'title': data.get('title', ''),
            'poster_path': data.get('poster_path', ''),
            'overview': data.get('overview', '')
        }
    )

    comments = movie.comments.all().order_by('-created_at')

    if request.method == 'POST' and request.session.get('username'):
        content = request.POST.get('content')
        if content:
            user = User.objects.get(username=request.session['username'])
            comment = Comment.objects.create(
                user=user,
                movie=movie,
                content=content
            )
            # Notify users who have this movie in their watchlist or commented on it
            watchlist_users = Watchlist.objects.filter(movie_id=movie_id).values_list('user', flat=True)
            commented_users = Comment.objects.filter(movie=movie).values_list('user', flat=True)
            notify_users = set(watchlist_users) | set(commented_users) - {user.id}  # Exclude the commenter
            for user_id in notify_users:
                notification_data = {
                    'user_id': user_id,
                    'message': f"New comment on '{movie.title}' by {user.username}",
                    'related_movie_id': movie.id
                }
                api_response = api_requests.post('http://localhost:5000/api/notifications', json=notification_data)
                if api_response.status_code != 201:
                    messages.error(request, 'Failed to create notification.')
            return redirect(f'/movies/?id={movie_id}')

    return render(request, 'movies.html', {  # Updated from Tvnerd/movies.html
        'data': data,
        'comments': comments,
    })

def tvshow_detail(request):
    tv_id = request.GET.get('id')
    if not tv_id:
        return redirect('tvshows')
    
    url = f'https://api.themoviedb.org/3/tv/{tv_id}?language=en-US'
    headers = {
        "accept": "application/json",
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI4N2JkNmRiZjI3ODRhZGU2ZDg3MjRhZTllMGFiYzRiYSIsIm5iZiI6MTczOTcwNTI0NS42NDcsInN1YiI6IjY3YjFjYjlkOGRjZTI5ZTNmYmUwZDM5ZiIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.QhC92XWnGlz7Ep5hshSkYhsF9S_DbqKYoZPWv8HYwe4"
    }
    
    response = api_requests.get(url, headers=headers)
    data = response.json() if response.status_code == 200 else {}
    
    credits_url = f'https://api.themoviedb.org/3/tv/{tv_id}/credits?language=en-US'
    credits_response = api_requests.get(credits_url, headers=headers)
    data['credits'] = credits_response.json() if credits_response.status_code == 200 else {'cast': [], 'crew': []}
    
    reviews_url = f'https://api.themoviedb.org/3/tv/{tv_id}/reviews?language=en-US'
    reviews_response = api_requests.get(reviews_url, headers=headers)
    data['reviews'] = reviews_response.json() if reviews_response.status_code == 200 else {'results': []}
    
    return render(request, 'shows.html', {  # Updated from Tvnerd/shows.html
        'data': data,
    })

def api_search_tv(request):
    query = request.GET.get('q', '')
    url = f"https://api.themoviedb.org/3/search/tv?query={query}&language=en-US&page=1"
    headers = {
        "accept": "application/json",
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI4N2JkNmRiZjI3ODRhZGU2ZDg3MjRhZTllMGFiYzRiYSIsIm5iZiI6MTczOTcwNTI0NS42NDcsInN1YiI6IjY3YjFjYjlkOGRjZTI5ZTNmYmUwZDM5ZiIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.QhC92XWnGlz7Ep5hshSkYhsF9S_DbqKYoZPWv8HYwe4"
    }
    response = api_requests.get(url, headers=headers)
    return JsonResponse(response.json().get('results', []), safe=False) if response.status_code == 200 else JsonResponse([], safe=False)

def watchlist_view(request):
    if 'username' not in request.session:
        return redirect('login')

    user = User.objects.get(username=request.session['username'])
    watchlist = Watchlist.objects.filter(user=user)

    return render(request, 'watchlist.html', {'watchlist': watchlist})  # Updated from Tvnerd/watchlist.html

def add_to_watchlist(request):
    if request.method == 'POST' and 'user_id' in request.session:
        user_id = request.session['user_id']
        movie_id = request.POST.get('movie_id')
        title = request.POST.get('title')
        poster_path = request.POST.get('poster_path')

        if not Watchlist.objects.filter(user_id=user_id, movie_id=movie_id).exists():
            Watchlist.objects.create(
                user_id=user_id,
                movie_id=movie_id,
                title=title,
                poster_path=poster_path
            )
            # Create notification via Flask API
            notification_data = {
                'user_id': user_id,
                'message': f"'{title}' added to your watchlist",
                'related_movie_id': Movie.objects.filter(tmdb_id=movie_id).first().id if Movie.objects.filter(tmdb_id=movie_id).exists() else None
            }
            api_response = api_requests.post('http://localhost:5000/api/notifications', json=notification_data)
            if api_response.status_code == 201:
                messages.success(request, f'"{title}" added to your watchlist.')
            else:
                messages.error(request, 'Failed to create notification.')
        else:
            messages.info(request, f'"{title}" is already in your watchlist.')

    return redirect(f"/movies/?id={movie_id}")

def remove_from_watchlist(request, movie_id):
    if 'user_id' not in request.session:
        return redirect('login')

    user_id = request.session['user_id']
    watchlist_item = Watchlist.objects.filter(user_id=user_id, movie_id=movie_id).first()
    if watchlist_item:
        title = watchlist_item.title
        watchlist_item.delete()
        # Create notification via Flask API
        notification_data = {
            'user_id': user_id,
            'message': f"'{title}' removed from your watchlist",
            'related_movie_id': Movie.objects.filter(tmdb_id=movie_id).first().id if Movie.objects.filter(tmdb_id=movie_id).exists() else None
        }
        api_response = api_requests.post('http://localhost:5000/api/notifications', json=notification_data)
        if api_response.status_code == 201:
            messages.success(request, 'Movie removed from watchlist.')
        else:
            messages.error(request, 'Failed to create notification.')
    return redirect('watchlist')

def news(request):
    return render(request, 'news.html')  # Updated from Tvnerd/news.html

def nominees(request):
    return render(request, 'nominees.html')  # Updated from Tvnerd/nominees.html

def video(request):
    return render(request, 'video.html')  # Updated from Tvnerd/video.html

def more(request):
    return render(request, 'awards.html')  # Updated from Tvnerd/awards.html

def celeb(request):
    return render(request, 'celeb.html')  # Updated from Tvnerd/celeb.html