from django.db import models

class Project(models.Model):
    PROJECT=(
        (1, 'Project 1'),
        (2, 'Project 2'),
        (3, 'Project 3'),
    )
    project_no=models.CharField(max_length=2,choices=PROJECT,default=1)

