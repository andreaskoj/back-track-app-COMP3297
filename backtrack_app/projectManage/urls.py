from django.urls import include, path
from . import views

urlpatterns = [
    path('', views.auth, name='projectManage'),
    path('create_project/', views.create_project, name='createProject'),
    path('invitation/', views.invitation, name='invitation'),
    path('invitation_form/', views.invitation_form, name='invitation'),

    # path('',views.ProjectManageManagement.as_view(), name='projectManage'),
    # path('logout',views.logout_view, name='noProject'),
    path('noProject',views.noProject.as_view(), name='noProject'),
    # path('createProject',views.createProject.as_view(), name='createProject'),
]
