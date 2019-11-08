from django.views.generic import TemplateView
from django.http import HttpResponse
from django.template.loader import render_to_string

# Create your views here.
class ProductBacklogManagement(TemplateView):
	template_name = "productBacklog/productBacklog.html"
#



