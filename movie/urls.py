from django.urls import path
from .views import Movielist , MovieDetailView

urlpatterns = [
    path('',Movielist.as_view(), name='movie_list'),
    path( "movie/deatail/<int:pk>/" , MovieDetailView.as_view(), name="movie_detail"),
]