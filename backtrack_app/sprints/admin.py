from django.contrib import admin

# Register your models here.
from .models import *
admin.site.register(SprintBacklog)
admin.site.register(PBI)
admin.site.register(Task)
admin.site.register(BurndownChart)
admin.site.register(SubTask)
admin.site.register(ScrumMaster)
admin.site.register(Project)
admin.site.register(Developer)