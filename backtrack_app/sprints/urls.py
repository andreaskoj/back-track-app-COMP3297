from django.contrib import admin
from django.urls import include, path
from . import views

urlpatterns = [
    path('<int:sprint>',views.SprintsManagement.as_view(), name='sprints'),
]
