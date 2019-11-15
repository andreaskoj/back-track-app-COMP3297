from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from .models import *
from django.contrib.auth.models import User


# Create your views here.
class SprintsManagement(TemplateView):
    template_name = "sprints/sprints.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['task_list'] = Task.objects.all()
        context['sprint'] = SprintBacklog.objects.get(pk=1)
        return context


class SprintBackLogsManagement(TemplateView):
    template_name = "sprints/sprintBacklogs.html"
    def get_context_data(self, **kwargs):
        pbi=self.kwargs['pbi']
        context = super().get_context_data(**kwargs)
        context['task_list']=Task.objects.filter(pbi__pk=pbi)
        context['pbi']=PBI.objects.get(pk=pbi)
        context['subtask_list']=SubTask.objects.filter(pbi__pk=pbi)
        context['pbiID']=pbi
        return context

class SprintCreate(TemplateView):
    template_name = "sprints/createsprint.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['pbi_list']=PBI.objects.all()
        return context

# def updateStatus(request):
#     pbi_status=str(request.POST['dropdown_status'])
#     PBI.objects.filter(pk=str(request.POST['pbiID'])).update(status=pbi_status)
#     # return redirect('http://127.0.0.1:8000/sprints')


def addSubtask(request):
    initialEstimatedEffort = str(request.POST['initialEstimatedEffort'])
    remaining_efforts = str(request.POST['remaining_efforts'])
    title = str(request.POST['title'])
    status = str(request.POST.get('status'))
    pbi = PBI.objects.get(pk=str(request.POST['pbiID']))
    SubTask.objects.create(initialEstimatedEffort = initialEstimatedEffort, 
             remaining_efforts = remaining_efforts, title = title, status = status, 
             pbi =pbi
            )
    #return render(request, 'pbi_list.html')
    return redirect('http://127.0.0.1:8000/sprints/pbi'+str(request.POST['pbiID']))

def createSprint(request):
    initialEf = str(request.POST['initialEf'])
    remainEf = str(request.POST['remainEf'])
    totalEf = str(request.POST['totalEf'])
    sprint = SprintBacklog.objects.create(initialEf = initialEf, 
             remainEf = remainEf, totalEf = totalEf, number=1
            )
    pbis = request.POST.getlist('pbis[]')
    for idx in pbis:
        PBI.objects.filter(id=idx).update(sprint =sprint)

    #return render(request, 'pbi_list.html')
    return redirect('http://127.0.0.1:8000/sprints')

def managePpl(request):
    idx = int(request.POST['id'])
    userId = int(request.POST['userId'])
    t =  str(request.POST['type'])
    subtask = SubTask.objects.get(id=idx)
    if t == "Join":
        subtask.Developers.add(Developer.objects.get(user=(User.objects.get(id=userId))))
    else:
        subtask.Developers.get(user=(User.objects.get(id=userId))).delete()

    
    return redirect('http://127.0.0.1:8000/sprints/pbi'+str(request.POST['pbiID']))
    




