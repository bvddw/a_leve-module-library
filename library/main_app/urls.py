from .views import *
from django.urls import path

urlpatterns = [
    path('login/', LoginUserView.as_view(), name='login_user_view'),
    path('register/', RegisterUserView.as_view(), name='register_user_view'),
    path('logout/', LogoutUserView.as_view(), name='logout_user_view'),
    path('profile/<str:username>/', UserProfileView.as_view(), name='user_profile_view'),
    path('profile/<str:username>/set-data/', SetUserDataView.as_view(), name='set_user_data_view'),
    path('profile/<str:username>/set-password/', SetUserPasswordView.as_view(), name='set_user_password_view'),
    path('password_changed/', PasswordChangedView.as_view(), name='password_changed_view'),
]
