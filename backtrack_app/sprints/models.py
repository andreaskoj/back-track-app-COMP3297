from django.db import models
from django.contrib.auth.models import User


class ScrumMaster(models.Model):
    user = models.OneToOneField(User, related_name="ScrumMaster", on_delete=models.CASCADE)

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
    number = models.IntegerField()
    objects = models.Manager()
    information = models.CharField(max_length=200, default="Description of the current sprint")
    totalEf = models.IntegerField(default=10, null=True)
    initialEf = models.IntegerField(default=10)
    remainEf = models.IntegerField(default=10, null=True)
    id = models.AutoField(primary_key=True)
    STATUS = (('C', 'created'), ('R', 'Removed'))
    status = models.CharField(max_length=10, choices=STATUS, default='created')

    # burndown = models.OneToOneField(BurndownChart, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.number)


class Project(models.Model):
    name = models.CharField(max_length=200)
    sprintNumber = models.IntegerField(default=0)
    id = models.AutoField(primary_key=True)
    master = models.ForeignKey(ScrumMaster, on_delete=models.SET_NULL, null=True)
    sprintBacklog = models.ForeignKey(SprintBacklog, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.name


class Developer(models.Model):
    user = models.OneToOneField(User, related_name="Developer", on_delete=models.CASCADE)
    isProductOwner = models.BooleanField(null=True, default=False)
    project = models.ForeignKey(Project, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.user.username


class PBI(models.Model):
    description = models.CharField(max_length=200)
    id = models.AutoField(primary_key=True)
    STATUS = (('NS', 'Not started'), ('IP', 'In progress'), ('C', 'Complete'), ('NF', 'Not Finished'))
    status = models.CharField(max_length=10, choices=STATUS, default='NS')
    sprint = models.ForeignKey(SprintBacklog, null=True, on_delete=models.SET_NULL, blank=True)
    estimated_efforts = models.IntegerField(null=True)
    remainStory = models.IntegerField(null=True, default=10)
    priority=models.IntegerField(default=0)
    objects = models.Manager()
    remaining_efforts=models.IntegerField(null=True)
    cumulative_storypoint=models.IntegerField(null=True, default=0, blank=True)

    # burndown=models.OneToOneField(BurndownChart, on_delete=models.CASCADE)
    def __str__(self):
        return self.description


class Task(models.Model):
    # description = models.CharField(max_length=200)
    id = models.AutoField(primary_key=True)
    # totalEf = models.IntegerField(default=10)
    # remainEf = models.IntegerField(default=10)
    pbi = models.ForeignKey(PBI, on_delete=models.CASCADE)
    objects = models.Manager()

    # burndown = models.OneToOneField(BurndownChart, on_delete=models.CASCADE)
    def __str__(self):
        return str(self.id)


class SubTask(models.Model):
    title = models.CharField(max_length=200)
    id = models.AutoField(primary_key=True)
    task = models.ForeignKey(Task, on_delete=models.CASCADE, null=True)
    pbi = models.ForeignKey(PBI, on_delete=models.CASCADE, related_name="SubTask", default=0)
    initialEstimatedEffort = models.IntegerField(null=True)
    remaining_efforts = models.IntegerField(null=True)
    Developers = models.ManyToManyField(Developer)
    STATUS = (('NS', 'Not started'), ('IP', 'In progress'), ('C', 'Complete'))
    status = models.CharField(max_length=10, choices=STATUS, default='IP')

    def __str__(self):
        return self.title

class Global_Data(models.Model):
    global_id = models.CharField(max_length=20, unique=True)
    current_ID = models.CharField(max_length=20)
    cumu_point = models.DecimalField(max_digits=6, decimal_places=0)
    num_pbis = models.DecimalField(max_digits=4, decimal_places=0)

    def __str__(self):
        return self.global_id