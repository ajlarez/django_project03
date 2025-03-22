from django.urls import path
from .views import Movielist

urlpatterns = [
    path('',Movielist.as_view(), name='movie_list')
]