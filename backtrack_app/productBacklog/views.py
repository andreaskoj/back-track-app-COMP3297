from django.conf import settings
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import TemplateView
from django.views.generic.list import ListView
# from functools import reduce
from django.views.generic import TemplateView
from sprints.models import PBI, Developer, ScrumMaster, Project, Global_Data


# from project.models import Product_Backlog_Item
# from project.models import Global_Data

# global_data = Global_Data.objects.get(global_id='00001')
# ID = int(global_data.current_ID)
# Total_point = int(global_data.cumu_point)
# Number = int(global_data.num_pbis)

# def productBacklog(request):
#     request

def product_backlog(request):
    if request.user.is_authenticated:
        user = str(request.user)
        if request.GET.get("DeletePBI"):
            pbi = PBI.objects.get(pk=int(request.GET.get('DeletePBI')))
            priority=pbi.priority
            pbi_list=PBI.objects.order_by('priority')
            for i in range(priority,len(pbi_list)):
                pbi_list[i].priority-=1
                pbi_list[i].save()
            pbi.delete()
        users_project = Developer.objects.filter(user__username=user)[0].project
        sprint_backlog = Project.objects.filter(name=users_project)[0].sprintBacklog
        pbis = PBI.objects.order_by('priority') # by default we show a full view of list of pbis
        for i in range(len(pbis)):
            if i==0:
                pbis[i].cumulative_storypoint=pbis[i].remainStory
                pbis[i].save()
            else:
                order=pbis[i].priority
                pbis[i].cumulative_storypoint=pbis[i].remainStory+pbis[i-1].cumulative_storypoint
                pbis[i].save()
        print(users_project)
        print(sprint_backlog)
        print(pbis)



        # print(project)
        return render(request, 'productBacklog/pbi_list.html', {'pbi_list': pbis})
        # return HttpResponse(user)

    else:
        return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))

def addPBI(request):
        # global Total_point
        # global ID
        # global Number
        # a = str(ID)
        # a = str(ID)
        # ID = ID + 1
        b = str(request.POST.get('title',False))
        d = request.POST.get('story_point', False)
        pbis = PBI.objects.order_by('priority')
        for pbi in pbis:
            pbi.priority+=1
            pbi.save()
        PBI.objects.create(remainStory=d, description=b, priority=0)
        # pbis = PBI.objects.order_by('priority')
        # return render(request, 'productBacklog/pbi_list.html', {'pbi_list': pbis})
        return redirect('http://127.0.0.1:8000/productBacklog')



# class pbiViewAll(TemplateView):
#     template_name = 'productBacklog/pbi_list.html'
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['pbi_list'] = PBI.objects.all()
#         return context
#
#     def home(request):
#         return redirect('http://127.0.0.1:8000/project/project')

    # def add(request):
    #     global Total_point
    #     global ID
    #     global Number
    #     a = str(ID)
    #     ID = ID + 1
    #     b = str(request.GET['title'])
    #     c = str(request.GET['detail'])
    #     d = request.GET['story_point']
    #     Total_point = Total_point + int(d)
    #     Number = Number + 1
    #     Global_Data.objects.filter(global_id='00001').update(current_ID=str(ID), cumu_point=Total_point,
    #                                                          num_pbis=Number)
    #     e = str(Total_point)
    #     f = str('Not Started')
    #     g = 0
    #     PBI.objects.create(
    #                                         title=b, detail=c, story_point=d,
    #                                         cumulative_story_point=e, status=f,
    #                                         priority=g)
    #     return redirect('/home/')


#
# def delete(request):
#     global Total_point
#     global Number
#     sid = request.GET.get('sid')
#     d = Product_Backlog_Item.objects.get(id_name = sid).story_point
#     Total_point = Total_point - int(d)
#     Number = Number - 1
#     Global_Data.objects.filter(global_id = '00001').update(cumu_point = Total_point, num_pbis = Number)
#     Product_Backlog_Item.objects.filter(id_name = sid).delete()
#     return redirect('/home/')
#
# def edit(request):
#     global Total_point
#     sid = request.GET.get('sid')
#     pbi = Product_Backlog_Item.objects.filter(id_name=sid).first()
#     d = Product_Backlog_Item.objects.get(id_name = sid).story_point
#     if request.method == 'POST':
#         title = request.POST.get('title')
#         detail = request.POST.get('detail')
#         story_point = request.POST.get('story_point')
#         status = request.POST.get('status')
#         Total_point = Total_point - int(d) + int(story_point)
#         Global_Data.objects.filter(global_id = '00001').update(cumu_point = Total_point)
#         Product_Backlog_Item.objects.filter(id_name=sid).update(title = title, detail = detail,
#                                                           story_point = story_point, status = status,
#                                                           cumulative_story_point = Total_point)
#         return redirect('/home/')
#     return render(request, 'pbi_edit.html', locals())
#
def edit(request):
    global Total_point
    sid = request.GET.get('sid')
    a = str(request.GET['id_name'])
    pbi = PBI.objects.get(id_name = a)
    #a = pbi.id_name
    Total_point = Total_point - int(pbi.story_point)
    b = str(request.GET['title'])
    c = str(request.GET['detail'])
    d = request.GET['story_point']
    Total_point = Total_point + int(d)
    Global_Data.objects.filter(global_id = '00001').update(cumu_point = Total_point)
    e = str(Total_point)
    f = str(request.GET['status'])
    PBI.objects.filter(id_name = a).update(
                                  description = b, estimated_efforts = d,
                                  status = f)
    return render(request, 'pbi_edit.html', locals())
#
#
# # def up(request):
# #     a = str(request.GET['id_name'])
# #     pbi = Product_Backlog_Item.objects.get(id_name = a)
# #     g = pbi.priority - 1
# #     Product_Backlog_Item.objects.filter(id_name = a).update(
# #                                   priority = g)
# #     return redirect('/home/')
#
# # def down(request):
# #     a = str(request.GET['id_name'])
# #     pbi = Product_Backlog_Item.objects.get(id_name = a)
# #     g = pbi.priority + 1
# #     Product_Backlog_Item.objects.filter(id_name = a).update(
# #                                   priority = g)
# #     return redirect('/home/')
#
# def full(request):
#     return redirect('/home/')
#
class pbiViewCurrent(TemplateView):
    template_name = 'pbi_list.html'
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['pbi_list'] = Product_Backlog_Item.objects.filter(status__in= ['Not Started', 'In Progress', 'Cancelled'])
#         return context
