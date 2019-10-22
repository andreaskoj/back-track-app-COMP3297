from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
class SprintsManagement(TemplateView): 
	template_name = "sprints/sprints.html"