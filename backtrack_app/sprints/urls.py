from django.contrib import admin
from django.urls import include, path
from django.conf.urls import  url
from . import views

urlpatterns = [
    path('',views.SprintsManagement.as_view(), name='sprints'),
    path('pbi<int:pbi>',views.SprintBackLogsManagement.as_view(), name='sprintBacklogs'),
     url(r'^addSubtask/$',views.addSubtask, name = 'addSubtask'),
]
