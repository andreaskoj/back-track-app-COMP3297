# Generated by Django 2.2.6 on 2019-11-08 13:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sprints', '0006_subtask_pbi'),
    ]

    operations = [
        migrations.AddField(
            model_name='subtask',
            name='status',
            field=models.CharField(choices=[('NS', 'Not started'), ('IP', 'In progress'), ('C', 'Complete')], default='IP', max_length=10),
        ),
    ]