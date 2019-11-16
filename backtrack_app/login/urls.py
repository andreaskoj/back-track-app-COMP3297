from django.contrib import admin
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    # default redirection
    path('', auth_views.LoginView.as_view(template_name='login/login.html'), name='backtrack-def'),

    path('login/', auth_views.LoginView.as_view(template_name='login/login.html'), name='backtrack-login'),
    path('logout/', auth_views.LogoutView.as_view(), name='backtrack-logout'),
]
