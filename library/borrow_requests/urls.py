from django.urls import path
from . import views

urlpatterns = [
    path('approve-request-book/<str:id>', views.ApproveRequestBookView.as_view(), name='approve_request_book_view'),
    path('decline-request-book/<str:id>', views.DeclineRequestBookView.as_view(), name='decline_request_book_view'),
    path('take-book/<str:id>', views.TakeBookView.as_view(), name='take_book_view'),
    path('return-book/<str:id>', views.ReturnBookView.as_view(), name='return_book_view'),
    path('borrow-request-history/', views.BorrowHistoryView.as_view(), name='borrow_request_history_view'),
]
