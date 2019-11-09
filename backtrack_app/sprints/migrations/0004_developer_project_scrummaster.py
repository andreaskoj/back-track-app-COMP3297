# Generated by Django 2.2.6 on 2019-11-08 11:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('sprints', '0003_auto_20191108_1009'),
    ]

    operations = [
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
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('master', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='sprints.ScrumMaster')),
            ],
        ),
        migrations.CreateModel(
            name='Developer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('isProductOwner', models.BooleanField(default=False, null=True)),
                ('project', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='sprints.Project')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='Developer', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
