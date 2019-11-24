from django.contrib import admin
from django.urls import include, path
from django.conf.urls import  url
from . import views

urlpatterns = [
    path('',views.SprintManagement, name='sprints'),
    path('pbi<int:pbi>',views.SprintBackLogsManagement.as_view(), name='sprintBacklogs'),
     url(r'^addSubtask/$',views.addSubtask, name = 'addSubtask'),
      path('createsprint',views.SprintCreate.as_view(), name='createsprints'),
      url(r'^createspri/$',views.createSprint, name = 'createSprint'),
      url(r'^managePpl/$',views.managePpl, name = 'managePpl'),
      url(r'^changesubtask/$',views.changesubtask, name = 'changesubtask'),
      url(r'^delsub/$',views.delsub, name = 'delsub'),
      url(r'^delsprint/$',views.delsprint, name = 'delsprint'),
      url(r'^changeremain/$',views.changeremain, name = 'changeremain'),
]
