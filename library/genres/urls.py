from django.urls import path
from .views import *

urlpatterns = [
    path('<str:name>/', GenreDetailView.as_view(), name='genre_detail_view'),
    path('create-genre', CreateGenreView.as_view(), name='create_genre_view'),
    path('update-genre/<str:name>', UpdateGenreView.as_view(), name='update_genre_view'),
    path('delete-genre/<str:name>', DeleteGenreView.as_view(), name='delete_genre_view'),
]