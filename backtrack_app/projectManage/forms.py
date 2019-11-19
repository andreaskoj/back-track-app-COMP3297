from django import forms
from sprints.models import Developer, ScrumMaster
from django.contrib.auth.models import User


class CreateProjectForm(forms.Form):
    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user')
        super(CreateProjectForm, self).__init__(*args, **kwargs)
        self.fields['developer'].choices = [(dev.user.username, dev.user.username) for dev in
                                            Developer.objects.exclude(user__username=user).filter(project=None)]

    project_name = forms.CharField(max_length=100)
    manager = forms.ChoiceField(choices=[(manager, manager) for manager in ScrumMaster.objects.all()])
    developer = forms.ChoiceField()

