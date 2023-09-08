from . import views
from django.urls import path

urlpatterns = [
    path('login/', views.LoginUserView.as_view(), name='login_user_view'),
    path('register/', views.RegisterUserView.as_view(), name='register_user_view'),
    path('logout/', views.LogoutUserView.as_view(), name='logout_user_view'),
    path('profile/<str:username>/', views.UserProfileView.as_view(), name='user_profile_view'),
    path('profile/<str:username>/set-data/', views.SetUserDataView.as_view(), name='set_user_data_view'),
    path('profile/<str:username>/set-password/', views.SetUserPasswordView.as_view(), name='set_user_password_view'),
    path('password_changed/', views.PasswordChangedView.as_view(), name='password_changed_view'),
]
