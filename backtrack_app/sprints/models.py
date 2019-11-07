from django.db import models


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
    # burndown = models.OneToOneField(BurndownChart, on_delete=models.CASCADE)
    def __str__(self):
        return str(self.number)

class PBI(models.Model):
    description=models.CharField(max_length=200)
    STATUS=(('NS','Not started'),('IP','In progress'),('C','Complete'))
    status=models.CharField(max_length=10,choices=STATUS, default='IP')
    sprint=models.ForeignKey(SprintBacklog, on_delete=models.CASCADE)
    objects = models.Manager()
    # burndown=models.OneToOneField(BurndownChart, on_delete=models.CASCADE)
    def __str__(self):
        return self.description

class Task(models.Model):
    description=models.CharField(max_length=200)
    pbi=models.ForeignKey(PBI, on_delete=models.CASCADE)
    objects = models.Manager()
    # burndown = models.OneToOneField(BurndownChart, on_delete=models.CASCADE)
    def __str__(self):
        return self.description




