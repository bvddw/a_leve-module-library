from django.urls import path
from .views import *

urlpatterns = [
    path('<str:name>/', AuthorDetailView.as_view(), name='author_detail_view'),
    path('create-author', CreateAuthorView.as_view(), name='create_author_view'),
    path('update-author/<str:name>', UpdateAuthorView.as_view(), name='update_author_view'),
    path('delete-author/<str:name>', DeleteAuthorView.as_view(), name='delete_author_view'),
]
