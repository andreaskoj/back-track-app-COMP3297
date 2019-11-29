import threading

from django.conf import settings
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.core.mail import EmailMessage
from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from sprints.models import Developer, ScrumMaster, Project
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render

from .forms import CreateProjectForm, JoinProject


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
                    # send_html_mail(address='kojandreas@gmail.com', project_name="Project1")
                    return render(request, 'projectManage/developer_main.html', {'withoutProjects': True,
                                                                                 'base': 'projectMana'
                                                                                         'ge/base.html',
                                                                                 'form': form,
                                                                                 })
                else:
                    # Developer - with project
                    project = user.project
                    return render(request, 'projectManage/developer_main.html', {'base': 'base_template.html',
                                                                                 'project': project,
                                                                                 })

        elif ScrumMaster.objects.filter(user__username=username).exists():

            # Manager
            return render(request, 'projectManage/manager_main.html')

        else:
            return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))


def invitation(request):
    project_name = request.GET['project']
    email = request.GET['email']

    form = JoinProject(project=project_name, email=email)

    return render(request, 'projectManage/join_project.html', {'p_name': project_name,
                                                               'form': form})


def invitation_form(request):
    if request.method == 'POST':
        form = JoinProject(request.POST, project='', email='')
        if form.is_valid():
            project = form.cleaned_data.pop("project")
            login = form.cleaned_data.pop("login")
            password = form.cleaned_data.pop("password")
            email = form.cleaned_data.pop("email")

            user = User.objects.create_user(username=login, email=email, password=password)

            dev = Developer(user=user)
            dev.project = Project.objects.get(name=project)
            dev.save()

            return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))


def create_project(request):
    if request.method == 'POST':
        form = CreateProjectForm(request.POST, user='')
        if form.is_valid():
            project_name = form.cleaned_data.pop("project_name")
            manager = form.cleaned_data.pop("manager")
            # developer = form.cleaned_data.pop("developer")

            devs = []
            developer_1 = form.cleaned_data.pop("Developer_1")
            if developer_1:
                devs.append(developer_1)
            developer_2 = form.cleaned_data.pop("Developer_2")
            if developer_2:
                devs.append(developer_2)
            developer_3 = form.cleaned_data.pop("Developer_3")
            if developer_3:
                devs.append(developer_3)

            new_project = Project(name=project_name)
            new_project.master = ScrumMaster.objects.get(user__username=manager)
            new_project.save()

            # dev = Developer.objects.get(user__username=developer)
            # dev.project = new_project
            # dev.save()

            po = Developer.objects.get(user__username=request.user.username)

            po.isProductOwner = True
            po.save()

            for dev in devs:
                send_html_mail(address=dev, project_name=project_name)

            return render(request, 'projectManage/developer_main.html', {'base': 'base_template.html'})


class EmailThread(threading.Thread):
    def __init__(self, subject, html_content, address):
        self.subject = subject
        self.address = address
        self.html_content = html_content
        threading.Thread.__init__(self)

    def run(self):
        msg = EmailMessage(subject=self.subject, body=self.html_content, to=[self.address])
        msg.content_subtype = "html"
        print(msg.send())


def send_html_mail(address, project_name):
    message = 'You are invited to ' + project_name + '!<br><br> To join it visit the following link: <a href="http://localhost:8000/projectManage/invitation?email=' + address + '&project=' + project_name + '"> Join ' + project_name + '</a>'
    subject = 'BackTrack: Welcome to ' + project_name + ' project'

    EmailThread(subject, message, address).start()


class ProjectManageManagement(TemplateView):
    template_name = "projectManage/projectManage.html"


class noProject(TemplateView):
    template_name = "projectManage/noProject.html"


class createProject(TemplateView):
    template_name = "projectManage/projectCreate.html"
