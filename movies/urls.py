from django.urls import path
from . import views

from django.urls import path
from . import views

urlpatterns = [
    path('', views.search_movies, name='movie_list'),
]
