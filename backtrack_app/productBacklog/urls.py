from django.contrib import admin
from django.urls import include, path
from productBacklog import views

# urlpatterns = [
#     path('', views.ProductBacklogManagement.as_view(), name='productBacklog'),
# ]

urlpatterns = [
    path('', views.pbiViewAll.as_view(), name='project'),
]
