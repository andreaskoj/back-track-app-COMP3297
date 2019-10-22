from django.contrib import admin
from django.urls import include, path
from projectManage import views

urlpatterns = [
    path('',views.ProjectManageManagement.as_view(), name='projectManage'),
]
