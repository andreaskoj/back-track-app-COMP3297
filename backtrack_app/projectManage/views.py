from django.conf import settings
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from sprints.models import Developer, ScrumMaster, Project
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
                    form = CreateProjectForm(user=username)
                    return render(request, 'projectManage/developer_main.html', {'withoutProjects': True,
                                                                                 'base': 'projectMana'
                                                                                         'ge/base.html',
                                                                                 'form': form
                                                                                 })
                else:
                    # Developer - with project
                    return render(request, 'projectManage/developer_main.html', {'base': 'base_template.html'})

        elif ScrumMaster.objects.filter(user__username=username).exists():
            # Manager
            return render(request, 'projectManage/manager_main.html')

        else:
            return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))


def create_project(request):
    if request.method == 'POST':
        form = CreateProjectForm(request.POST, user='')
        if form.is_valid():

            project_name = form.cleaned_data.pop("project_name")
            manager = form.cleaned_data.pop("manager")
            developer = form.cleaned_data.pop("developer")

            new_project = Project(name=project_name)
            new_project.master = ScrumMaster.objects.get(user__username=manager)
            new_project.save()

            dev = Developer.objects.get(user__username=developer)
            dev.project = new_project
            dev.save()

            po = Developer.objects.get(user__username=request.user.username)

            po.isProductOwner = True
            po.save()

            return render(request, 'projectManage/developer_main.html', {'base': 'base_template.html'})


class ProjectManageManagement(TemplateView):
    template_name = "projectManage/projectManage.html"


class noProject(TemplateView):
    template_name = "projectManage/noProject.html"


class createProject(TemplateView):
    template_name = "projectManage/projectCreate.html"
