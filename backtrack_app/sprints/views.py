from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from .models import *
from django.contrib.auth.models import User
import json


def SprintManagement(request):
    if len(SprintBacklog.objects.filter(status='created')) == 0:
        return redirect('http://127.0.0.1:8000/sprints/createsprint')
    sprint = SprintBacklog.objects.get(status='created')
    # sprint=SprintBacklog.objects.all()
    if request.GET.get("DeleteButton"):
        task=Task.objects.get(pk=int(request.GET.get('DeleteButton')))
        remainingEfforts=task.pbi.estimated_efforts
        pbi_id=task.pbi.id
        task.delete()
        pbi=PBI.objects.get(pk=pbi_id)
        if int(remainingEfforts) > 0:
            pbi.status="NS"
        else:
            pbi.status="C"
        pbi.save()
    tasks=Task.objects.all()
    for i in tasks:
        pbi_index=i.pbi.id
        pbi_update=PBI.objects.get(pk=pbi_index)
        subtask_list=SubTask.objects.filter(pbi__pk=pbi_index)
        remaining=0
        for subtask in subtask_list:
            remaining+=subtask.remaining_efforts
        if remaining>0 or len(subtask_list)==0:
            pbi_update.status="IP"
        else:
            pbi_update.status="C"
        pbi_update.remaining_efforts=remaining
        pbi_update.save()
    if request.method=="POST":
        info=request.POST.get('information_of_sprint',False)
        sprint.information=info
        sprint.save()
        # pbi_id=request.POST.get()
    return render(request,'sprints/sprints.html',{'task_list':tasks,'sprint':sprint})


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
        pbi_list=PBI.objects.order_by('priority')
        context['pbi_list']=list(filter(lambda x: x.status=="NS",pbi_list))
        return context


def updateStatus(request):
    pbi_status=str(request.GET['dropdown_status'])
    PBI.objects.filter(pk=request.GET['pbiID']).update(status=pbi_status)
    # return redirect('http://127.0.0.1:8000/sprints')


def addSubtask(request):
    initialEstimatedEffort = str(request.POST['initialEstimatedEffort'])
    title = str(request.POST['title'])
    status = str(request.POST.get('status'))
    pbi = PBI.objects.get(pk=str(request.POST['pbiID']))
    SubTask.objects.create(initialEstimatedEffort = initialEstimatedEffort, 
             remaining_efforts = initialEstimatedEffort, title = title, status = status, 
             pbi =pbi
            )
    #return render(request, 'pbi_list.html')
    return redirect('http://127.0.0.1:8000/sprints/pbi'+str(request.POST['pbiID']))


def createSprint(request):
    initialEf = str(request.POST['initialEf'])
    remainEf = str(request.POST['remainEf'])
    totalEf = str(request.POST['totalEf'])
    if SprintBacklog.objects.count==0:
        number=1
    else:
        latest=SprintBacklog.objects.order_by('-number')[0]
        number=latest.number+1
    sprint = SprintBacklog.objects.create(initialEf = initialEf, 
             remainEf = totalEf, totalEf = totalEf, number=number, status='created'
            )
    pbis = request.POST.getlist('pbis[]')
    for idx in pbis:
        pbi=PBI.objects.get(id=idx)
        PBI.objects.filter(id=idx).update(sprint =sprint,remaining_efforts=pbi.estimated_efforts)

        Task.objects.create(pbi = PBI.objects.get(id=idx))

    #return render(request, 'pbi_list.html')
    return redirect('http://127.0.0.1:8000/sprints/')

def managePpl(request):
    idx = int(request.POST['id'])
    userId = int(request.POST['userId'])
    t =  str(request.POST['type'])
    subtask = SubTask.objects.get(id=idx)
    if t == "Join":
        subtask.Developers.add(Developer.objects.get(user=(User.objects.get(id=userId))))
    else:
        subtask.Developers.remove((Developer.objects.get(user=(User.objects.get(id=userId)))))
    if subtask.status == "NS":
        subtask.status = "IP"
        subtask.save()
    return HttpResponse("")

def delsub(request):
    idx = int(request.POST['id'])
    SubTask.objects.get(id=idx).delete()
    return HttpResponse("")
    

def delsprint(request):
    if request.method=="POST":
        sprint=SprintBacklog.objects.get(number=int(request.POST.get("sprintNumber", False)))
        sprint.status='Removed'
        sprint.save()
    # SprintBacklog.objects.all().delete()
    tasks = Task.objects.all()
    for task in tasks:

        remaining=0
        total=0
        pbi_id=task.pbi.id
        subtask_list=SubTask.objects.filter(pbi__pk=pbi_id)
        for subtask in subtask_list:
            remaining+=subtask.remaining_efforts
            total+=subtask.initialEstimatedEffort
        task.delete()
        pbi=PBI.objects.get(pk=pbi_id)
        if total-remaining > 0:
            pbi.status="NF"
        else:
            pbi.status="NS"
        pbi.save()
    return redirect('http://127.0.0.1:8000/sprints')

def changesubtask(request):
    idx = int(request.POST['id'])
    status =  str(request.POST['status'])
    SubTask.objects.filter(id=idx).update(status=status)
    return HttpResponse("")


def changeremain(request):
    idx = int(request.POST['id'])
    remain =  str(request.POST['remain'])
    SubTask.objects.filter(id=idx).update(remaining_efforts=remain)
    return redirect('http://127.0.0.1:8000/sprints/pbi'+str(request.POST['pbiID']))
