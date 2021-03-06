# Generated by Django 2.2.6 on 2019-12-07 01:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='BurndownChart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estimated_efforts', models.IntegerField()),
                ('remaining_efforts', models.IntegerField()),
                ('burndown_efforts', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Developer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('isProductOwner', models.BooleanField(default=False, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Global_Data',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('global_id', models.CharField(max_length=20, unique=True)),
                ('current_ID', models.CharField(max_length=20)),
                ('cumu_point', models.DecimalField(decimal_places=0, max_digits=6)),
                ('num_pbis', models.DecimalField(decimal_places=0, max_digits=4)),
            ],
        ),
        migrations.CreateModel(
            name='PBI',
            fields=[
                ('description', models.CharField(max_length=200)),
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('status', models.CharField(choices=[('NS', 'Not started'), ('IP', 'In progress'), ('C', 'Complete'), ('NF', 'NotFinish')], default='NS', max_length=10)),
                ('estimated_efforts', models.IntegerField(null=True)),
                ('remainStory', models.IntegerField(default=10, null=True)),
                ('priority', models.IntegerField(default=0, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='SprintBacklog',
            fields=[
                ('number', models.IntegerField()),
                ('information', models.CharField(default='Description of the current sprint', max_length=200)),
                ('totalEf', models.IntegerField(default=10, null=True)),
                ('initialEf', models.IntegerField(default=10)),
                ('remainEf', models.IntegerField(default=10, null=True)),
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('status', models.CharField(choices=[('C', 'created'), ('R', 'Removed')], default='created', max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('pbi', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sprints.PBI')),
            ],
        ),
        migrations.CreateModel(
            name='SubTask',
            fields=[
                ('title', models.CharField(max_length=200)),
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('initialEstimatedEffort', models.IntegerField(null=True)),
                ('remaining_efforts', models.IntegerField(null=True)),
                ('status', models.CharField(choices=[('NS', 'Not started'), ('IP', 'In progress'), ('C', 'Complete')], default='IP', max_length=10)),
                ('Developers', models.ManyToManyField(to='sprints.Developer')),
                ('pbi', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='SubTask', to='sprints.PBI')),
                ('task', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='sprints.Task')),
            ],
        ),
        migrations.CreateModel(
            name='ScrumMaster',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='ScrumMaster', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('name', models.CharField(max_length=200)),
                ('sprintNumber', models.IntegerField(default=0)),
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('master', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='sprints.ScrumMaster')),
                ('sprintBacklog', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='sprints.SprintBacklog')),
            ],
        ),
        migrations.AddField(
            model_name='pbi',
            name='sprint',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='sprints.SprintBacklog'),
        ),
        migrations.AddField(
            model_name='developer',
            name='project',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='sprints.Project'),
        ),
        migrations.AddField(
            model_name='developer',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='Developer', to=settings.AUTH_USER_MODEL),
        ),
    ]
