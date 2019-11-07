from django.contrib import admin

# Register your models here.
from .models import *
admin.site.register(SprintBacklog)
admin.site.register(PBI)
admin.site.register(Task)
admin.site.register(BurndownChart)