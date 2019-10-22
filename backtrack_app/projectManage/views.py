from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
class ProjectManageManagement(TemplateView): 
	template_name = "projectManage/projectManage.html"