from django.urls import path
from .views import *

urlpatterns = [
    path('<str:isbn>/', BookDetailView.as_view(), name='book_detail_view'),
    path('create-book', CreateBookView.as_view(), name='create_book_view'),
    path('update-book/<str:isbn>', UpdateBookView.as_view(), name='update_book_view'),
    path('delete-book/<str:isbn>', DeleteBookView.as_view(), name='delete_book_view'),
    path('<str:isbn>/request-book/', RequestBookView.as_view(), name='request_book_view'),
]
