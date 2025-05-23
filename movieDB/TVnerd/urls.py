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
    path('tvshows/', views.tvshow, name='tvshows'),    
    path('watchlist/', views.watchlist_view, name='watchlist'),
    path('watchlist/add/', views.add_to_watchlist, name='add_to_watchlist'),
    path('watchlist/remove/<str:movie_id>/', views.remove_from_watchlist, name='remove_from_watchlist'),
    path('nominees/', views.nominees, name='nominees'),
    path('news/', views.news, name='news'),
    path('video/', views.video, name='video'),
    path('tvshows/show/', views.tvshow_detail, name='tvshow_detail'),
    path('api/search/tv/', views.api_search_tv, name='api_search_tv'),
    path('celeb/', views.popular_celebs, name='popular_celebs'),
    path('celeb/<int:celeb_id>/', views.celeb_detail, name='celeb_detail'),


]

   