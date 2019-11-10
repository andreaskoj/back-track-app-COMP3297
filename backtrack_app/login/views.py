from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponse


# Create your views here.
class LoginManagement(TemplateView):
    template_name = "login/login.html"

