from django.contrib import admin
from django.urls import include, path
from login import views

urlpatterns = [
    path('',views.LoginManagement.as_view(), name='login'),
]
