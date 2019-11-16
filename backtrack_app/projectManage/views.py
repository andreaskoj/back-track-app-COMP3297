from django.conf import settings
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from sprints.models import Developer, ScrumMaster
from django.http import HttpResponseRedirect
from django.shortcuts import render

from .forms import CreateProjectForm


def is_member(user):
    return user.groups.filter(name='developer').exists()


def auth(request):
    if request.user.is_authenticated:

        # get logged in username
        username = request.user.username

        if Developer.objects.filter(user__username=username).exists():
            user = Developer.objects.get(user__username=username)
            if user.isProductOwner:
                # Product owner
                return render(request, 'projectManage/po_main.html')
            else:
                if user.project is None:
                    # Developer - without project
                    return render(request, 'projectManage/developer_main.html', {'withoutProjects': True,
                                                                                 'base': 'projectManage/base.html'})
                else:
                    # Developer - with project
                    return render(request, 'projectManage/developer_main.html', {'base': 'base_template.html'})

        elif ScrumMaster.objects.filter(user__username=username).exists():
            # Manager
            return render(request, 'projectManage/manager_main.html')

        else:
            return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))


def create_project(request):
    # print("TEST")
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        print("TEST")
        # create a form instance and populate it with data from the request:
        form = CreateProjectForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/thanks/')

    # if a GET (or any other method) we'll create a blank form
    else:
        print("TEST2")
        form = CreateProjectForm()

    return render(request, 'projectManage/developer_main.html', {'withoutProjects': True,
                                                                 'base': 'projectManage/base.html',
                                                                 'form': form})


class ProjectManageManagement(TemplateView):
    template_name = "projectManage/projectManage.html"


class noProject(TemplateView):
    template_name = "projectManage/noProject.html"


class createProject(TemplateView):
    template_name = "projectManage/projectCreate.html"
