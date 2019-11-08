from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from .models import SprintBacklog, PBI, Task, SubTask


# Create your views here.
class SprintsManagement(TemplateView):
    template_name = "sprints/sprints.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['pbi_list'] = PBI.objects.filter()
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
    return redirect('http://127.0.0.1:8000/sprints/pbi1')
