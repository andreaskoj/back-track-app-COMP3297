from django.contrib import admin
from django.urls import include, path
from . import views

urlpatterns = [
    path('',views.SprintsManagement.as_view(), name='sprints'),
    path('sprintBacklog',views.SprintBackLogsManagement.as_view(), name='sprintBacklogs'),

]
