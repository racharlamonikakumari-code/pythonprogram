from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('welcome/', views.welcome, name='welcome'),
    path('logout/', views.logout_view, name='logout'),

    # Login
    path('login/', auth_views.LoginView.as_view(
        template_name='studentapp/login.html'), name='login'),

    # Password Change
    path('password_change/', auth_views.PasswordChangeView.as_view(
        template_name='studentapp/password_change.html',
        success_url='/login/'), name='password_change'),

    # Password Reset
    path('password_reset/', auth_views.PasswordResetView.as_view(
        template_name='studentapp/password_reset.html'), name='password_reset'),

    path('password_reset_done/', auth_views.PasswordResetDoneView.as_view(
        template_name='studentapp/password_reset_done.html'), name='password_reset_done'),
]
