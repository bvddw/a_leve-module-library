from django.urls import path
from .views import *

urlpatterns = [
    path('approve-request-book/<str:id>', ApproveRequestBookView.as_view(), name='approve_request_book_view'),
    path('decline-request-book/<str:id>', DeclineRequestBookView.as_view(), name='decline_request_book_view'),
    path('take-book/<str:id>', TakeBookView.as_view(), name='take_book_view'),
    path('return-book/<str:id>', ReturnBookView.as_view(), name='return_book_view'),
    path('borrow-request-history/', BorrowHistoryView.as_view(), name='borrow_request_history_view'),
]
