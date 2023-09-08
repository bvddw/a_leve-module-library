from django.urls import path
from . import views

urlpatterns = [
    path('<str:name>/', views.AuthorDetailView.as_view(), name='author_detail_view'),
    path('create-author', views.CreateAuthorView.as_view(), name='create_author_view'),
    path('update-author/<str:name>', views.UpdateAuthorView.as_view(), name='update_author_view'),
    path('delete-author/<str:name>', views.DeleteAuthorView.as_view(), name='delete_author_view'),
]
