from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login_view, name='login'),
    path('signup/', views.signup_view, name='signup'),
    path('logout/', views.logout_view, name='logout'),
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('movies/', views.movies_view, name='movies'),
    path('api/search/', views.api_search, name='api_search'),
    path('awards/', views.more, name='awards'),
    path('celeb/', views.celeb, name='celeb'),
    path('tvshows/', views.tvshow, name='tvshows'),
]