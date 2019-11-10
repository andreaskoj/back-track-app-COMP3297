from django.db import models
from django.contrib.auth.models import User

class ScrumMaster(models.Model):
    user=models.OneToOneField(User,related_name="ScrumMaster",on_delete=models.CASCADE)
    def __str__(self):
        return self.user.username

class Project(models.Model):
    name=models.CharField(max_length=200)
    id=models.AutoField(primary_key=True)
    master=models.ForeignKey(ScrumMaster, on_delete=models.SET_NULL, null=True)
    def __str__(self):
        return self.name

class Developer(models.Model):
    user=models.OneToOneField(User,related_name="Developer",on_delete=models.CASCADE)
    isProductOwner = models.BooleanField(null=True, default=False)
    project = models.ForeignKey(Project, on_delete=models.SET_NULL, null=True)
    def __str__(self):
        return self.user.username

class BurndownChart(models.Model):
    estimated_efforts = models.IntegerField()
    remaining_efforts = models.IntegerField()
    burndown_efforts = models.IntegerField()
    objects = models.Manager()

    def __str__(self):
        return f'{self.estimated_efforts} {self.remaining_efforts} {self.burndown_efforts}'

class SprintBacklog(models.Model):
    number=models.IntegerField()
    objects=models.Manager()
    totalEf = models.IntegerField(default=10)
    averageEf = models.IntegerField(default=10)
    initialEf = models.IntegerField(default=10)
    remainEf = models.IntegerField(default=10)
    id=models.AutoField(primary_key=True)
    # burndown = models.OneToOneField(BurndownChart, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.number)

class PBI(models.Model):
    description=models.CharField(max_length=200)
    id=models.AutoField(primary_key=True)
    STATUS=(('NS','Not started'),('IP','In progress'),('C','Complete'))
    status=models.CharField(max_length=10,choices=STATUS, default='IP')
    sprint=models.ForeignKey(SprintBacklog, null=True,on_delete=models.SET_NULL)
    estimated_efforts = models.IntegerField(null=True)
    objects = models.Manager()
    # burndown=models.OneToOneField(BurndownChart, on_delete=models.CASCADE)
    def __str__(self):
        return self.description

class Task(models.Model):
    description=models.CharField(max_length=200)
    id=models.AutoField(primary_key=True)
    totalEf = models.IntegerField(default=10)
    remainEf = models.IntegerField(default=10)
    pbi=models.ForeignKey(PBI, on_delete=models.CASCADE)
    objects = models.Manager()
    # burndown = models.OneToOneField(BurndownChart, on_delete=models.CASCADE)
    def __str__(self):
        return self.description

class SubTask(models.Model):
    title=models.CharField(max_length=200)
    id=models.AutoField(primary_key=True)
    task=models.ForeignKey(Task, on_delete=models.CASCADE,null=True)
    pbi=models.ForeignKey(PBI, on_delete=models.CASCADE,related_name="SubTask",default=0)
    initialEstimatedEffort = models.IntegerField(null=True)
    remaining_efforts = models.IntegerField(null=True)
    Developers = models.ManyToManyField(Developer,  null=True)
    STATUS=(('NS','Not started'),('IP','In progress'),('C','Complete'))
    status=models.CharField(max_length=10,choices=STATUS, default='IP')
    def __str__(self):
        return self.title








