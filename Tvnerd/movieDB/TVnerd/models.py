from django.db import models

class User(models.Model):
    username = models.CharField(max_length=150, unique=True)
    password = models.CharField(max_length=200)
    email = models.EmailField()

    def __str__(self):
        return self.username
    

class Watchlist(models.Model):
    user = models.ForeignKey('User', on_delete=models.CASCADE)
    movie_id = models.CharField(max_length=20)
    title = models.CharField(max_length=255)
    poster_path = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.title} (User {self.user_id})"