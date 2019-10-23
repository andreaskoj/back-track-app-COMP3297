from django.contrib import admin
from django.urls import include, path
from projectManage import views

urlpatterns = [
    path('',views.ProjectManageManagement.as_view(), name='projectManage'),
    path('noProject',views.noProject.as_view(), name='noProject'),
    path('createProject',views.createProject.as_view(), name='createProject'),
]
