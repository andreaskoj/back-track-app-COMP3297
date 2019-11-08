from django.contrib import admin
from django.urls import include, path
from . import views

urlpatterns = [
    path('<int: pbi>',views.TaskManagement.as_view(), name='tasks'),
]
