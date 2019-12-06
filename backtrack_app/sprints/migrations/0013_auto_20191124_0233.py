# Generated by Django 2.2.6 on 2019-11-24 02:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sprints', '0012_auto_20191115_0730'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sprintbacklog',
            name='averageEf',
        ),
        migrations.AddField(
            model_name='sprintbacklog',
            name='information',
            field=models.CharField(default='Description of the current sprint', max_length=200),
        ),
        migrations.AddField(
            model_name='sprintbacklog',
            name='status',
            field=models.CharField(choices=[('C', 'created'), ('R', 'Removed')], default='created', max_length=10),
        ),
        migrations.AlterField(
            model_name='pbi',
            name='status',
            field=models.CharField(choices=[('NS', 'Not started'), ('IP', 'In progress'), ('C', 'Complete'), ('F', 'Finished')], default='NS', max_length=10),
        ),
        migrations.AlterField(
            model_name='sprintbacklog',
            name='remainEf',
            field=models.IntegerField(default=10, null=True),
        ),
        migrations.AlterField(
            model_name='sprintbacklog',
            name='totalEf',
            field=models.IntegerField(default=10, null=True),
        ),
    ]