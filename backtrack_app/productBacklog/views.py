from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
class ProductBacklogManagement(TemplateView):
	template_name = "productBacklog/login.html"

