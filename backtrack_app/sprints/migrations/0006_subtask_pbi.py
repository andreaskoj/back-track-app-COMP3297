# Generated by Django 2.2.6 on 2019-11-08 13:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sprints', '0005_subtask_developers'),
    ]

    operations = [
        migrations.AddField(
            model_name='subtask',
            name='pbi',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='SubTask', to='sprints.PBI'),
        ),
    ]