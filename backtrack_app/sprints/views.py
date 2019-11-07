from django.shortcuts import render
from django.views.generic import TemplateView
from .models import SprintBacklog, PBI

# Create your views here.
class SprintsManagement(TemplateView): 
	template_name = "sprints/sprints.html"
	def get_context_data(self, **kwargs):
		sprint=self.kwargs['sprint']
		context=super().get_context_data(**kwargs)
		context['pbi_list']=PBI.objects.filter(sprint__pk=sprint)
		context['sprint']=SprintBacklog.objects.get(pk=sprint)
		return context