from django.urls import path
from members import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('register/',views.UserRegView.as_view(), name='register'),
    path('profile/',views.ProfileView.as_view(), name='profile'),
    path('password/',views.PasswordView.as_view(), name='password'),
]
