from django.conf import settings
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from sprints.models import Developer, ScrumMaster


def is_member(user):
    return user.groups.filter(name='developer').exists()


def auth(request):

    if request.user.is_authenticated:

        # get logged in username
        username = request.user.username

        if Developer.objects.filter(user__username=username).exists():
            user = Developer.objects.get(user__username=username)
            if user.isProductOwner:
                return render(request, 'projectManage/po_main.html')
            else:
                if user.project is None:
                    return render(request, 'projectManage/developer_main.html', {'withoutProjects': True, 'base': 'projectManage/base.html'})
                else:
                    return render(request, 'projectManage/developer_main.html', {'base': 'base_template.html'})
        elif ScrumMaster.objects.filter(user__username=username).exists():
            return render(request, 'projectManage/manager_main.html')

        else:
            return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))


class ProjectManageManagement(TemplateView):
    template_name = "projectManage/projectManage.html"


class noProject(TemplateView):
    template_name = "projectManage/noProject.html"


class createProject(TemplateView):
    template_name = "projectManage/projectCreate.html"
