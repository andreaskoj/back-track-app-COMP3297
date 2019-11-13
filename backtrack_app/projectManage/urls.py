from django.urls import include, path
from . import views

urlpatterns = [
    path('', views.auth, name='projectManage'),

    # path('',views.ProjectManageManagement.as_view(), name='projectManage'),
    # path('logout',views.logout_view, name='noProject'),
    path('noProject',views.noProject.as_view(), name='noProject'),
    path('createProject',views.createProject.as_view(), name='createProject'),
]
