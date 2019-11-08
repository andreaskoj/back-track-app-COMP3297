from django.shortcuts import render
from django.views.generic import TemplateView
from .models import SprintBacklog, PBI

# Create your views here.
class SprintsManagement(TemplateView): 
	template_name = "sprints/sprints.html"
	def get_context_data(self, **kwargs):
		context=super().get_context_data(**kwargs)
		context['pbi_list']=PBI.objects.filter()
		context['sprint']=SprintBacklog.objects.get(pk=1)
		return context
