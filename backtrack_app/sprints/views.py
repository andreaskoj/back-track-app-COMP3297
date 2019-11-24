from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from .models import *
from django.contrib.auth.models import User
import json


def SprintManagement(request):
    if SprintBacklog.objects.count() == 0:
    	return redirect('http://127.0.0.1:8000/sprints/createsprint')
    sprint = SprintBacklog.objects.get(number=1)
    if request.GET.get("DeleteButton"):
        task=Task.objects.get(pk=int(request.GET.get('DeleteButton')))
        remainingEfforts=task.pbi.remainStory
        pbi_id=task.pbi.id
        task.delete()
        pbi=PBI.objects.get(pk=pbi_id)
        if int(remainingEfforts) > 0:
            pbi.status="NS"
        else:
            pbi.status="F"
        pbi.save()
    tasks=Task.objects.all()
    for i in tasks:
        pbi_index=i.pbi.id
        pbi_update=PBI.objects.get(pk=pbi_index)
        pbi_update.status="IP"
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
        context['pbi_list']=PBI.objects.all()
        return context


def updateStatus(request):
    pbi_status=str(request.GET['dropdown_status'])
    PBI.objects.filter(pk=request.GET['pbiID']).update(status=pbi_status)
    # return redirect('http://127.0.0.1:8000/sprints')


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
             remainEf = totalEf, totalEf = totalEf, number=1
            )
    pbis = request.POST.getlist('pbis[]')
    for idx in pbis:
        PBI.objects.filter(id=idx).update(sprint =sprint)
        Task.objects.create(pbi = PBI.objects.get(id=idx))

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
    SprintBacklog.objects.all().delete()
    tasks = Task.objects.all()
    for task in tasks:
    	remainingEfforts=task.pbi.remainStory
    	pbi_id=task.pbi.id
    	task.delete()
    	pbi=PBI.objects.get(pk=pbi_id)
    	if int(remainingEfforts) > 0:
    		pbi.status="NS"
    	else:
    		pbi.status="F"
    	pbi.save()
    return redirect('http://127.0.0.1:8000/sprints')

def changesubtask(request):
    idx = int(request.POST['id'])
    status =  str(request.POST['status'])
    SubTask.objects.filter(id=idx).update(status=status)
    return HttpResponse("")

