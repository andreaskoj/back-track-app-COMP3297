from django.db import models

# Create your models here.
class Project(models.Model):
    name = models.CharField(max_length=30)

class Deverloper(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    project = models.ForeignKey(Project,on_delete=models.SET_NULL, blank=True, null=True)


