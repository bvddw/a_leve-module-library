from django.urls import path
from . import views

urlpatterns = [
    path('<str:isbn>/', views.BookDetailView.as_view(), name='book_detail_view'),
    path('create-book', views.CreateBookView.as_view(), name='create_book_view'),
    path('update-book/<str:isbn>', views.UpdateBookView.as_view(), name='update_book_view'),
    path('delete-book/<str:isbn>', views.DeleteBookView.as_view(), name='delete_book_view'),
    path('<str:isbn>/request-book/', views.RequestBookView.as_view(), name='request_book_view'),
]
