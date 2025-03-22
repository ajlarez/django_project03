from django.shortcuts import render
from django.views.generic import ListView, DetailView
from movie.models import Pelicula
# Create your views here.

class Movielist(ListView):
    model = Pelicula
    template_name = 'Movies/movie_list.html'

