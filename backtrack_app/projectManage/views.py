from django.conf import settings
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import TemplateView


def is_member(user):
    return user.groups.filter(name='developer').exists()


def detail(request):
    # checking if the user is authenticated
    print(is_member(request.user))

    if not request.user.is_authenticated:
        return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))
    else:
        if request.user.groups.filter(name='developer').exists():
            return render(request, 'projectManage/developer_main.html')

        elif request.user.groups.filter(name='product_owner').exists():
            return render(request, 'projectManage/po_main.html')

        elif request.user.groups.filter(name='manager').exists():
            return render(request, 'projectManage/manager_main.html')

        else:
            print("This user dont belong to any group")


class ProjectManageManagement(TemplateView):
    template_name = "projectManage/projectManage.html"


class noProject(TemplateView):
    template_name = "projectManage/noProject.html"


class createProject(TemplateView):
    template_name = "projectManage/projectCreate.html"
