from django import forms
from sprints.models import Developer, ScrumMaster


class CreateProjectForm(forms.Form):
    project_name = forms.CharField(max_length=100)
    manager = forms.ChoiceField(choices=[(dev.user.username, dev.user.username) for dev in ScrumMaster.objects.all()])
    developer = forms.ChoiceField(choices=[(dev.user.username, dev.user.username) for dev in Developer.objects.all()])
