from django.contrib import admin
from django.urls import include, path
from . import views
from django.conf.urls import  url


# urlpatterns = [
#     path('', views.ProductBacklogManagement.as_view(), name='productBacklog'),
# ]

urlpatterns = [
    # path('', views.pbiViewAll.as_view(), name='project'),
    path('', views.product_backlog , name='productBacklog'),
    url(r'^add/$',views.addPBI, name = 'addPBI'),
]
