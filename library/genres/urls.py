from django.urls import path
from . import views

urlpatterns = [
    path('<str:name>/', views.GenreDetailView.as_view(), name='genre_detail_view'),
    path('create-genre', views.CreateGenreView.as_view(), name='create_genre_view'),
    path('update-genre/<str:name>', views.UpdateGenreView.as_view(), name='update_genre_view'),
    path('delete-genre/<str:name>', views.DeleteGenreView.as_view(), name='delete_genre_view'),
]