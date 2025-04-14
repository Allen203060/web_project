from django.db import models
from django.contrib.auth.models import User    

class User(models.Model):
    username = models.CharField(max_length=150, unique=True)
    password = models.CharField(max_length=200)
    email = models.EmailField()

    def __str__(self):
        return self.username
    

class Movie(models.Model):
    tmdb_id = models.IntegerField(unique=True)  # Links to TMDB movie ID
    title = models.CharField(max_length=255)
    poster_path = models.CharField(max_length=255, blank=True)
    overview = models.TextField(blank=True)

    def __str__(self):
        return self.title
    

class Comment(models.Model):
    user = models.ForeignKey('User', on_delete=models.CASCADE)  # Use your custom User model
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='comments')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)


class Watchlist(models.Model):
    user = models.ForeignKey('User', on_delete=models.CASCADE)
    movie_id = models.CharField(max_length=20)
    title = models.CharField(max_length=255)
    poster_path = models.CharField(max_length=255, null=True)

    def __str__(self):
        return f"{self.title} (User {self.user_id})"

    

