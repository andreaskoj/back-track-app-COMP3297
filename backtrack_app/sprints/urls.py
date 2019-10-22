from django.contrib import admin
from django.urls import include, path
from sprints import views

urlpatterns = [
    path('',views.SprintsManagement.as_view(), name='sprints'),
]
