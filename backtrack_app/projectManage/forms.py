from django import forms
from sprints.models import Developer, ScrumMaster


class CreateProjectForm(forms.Form):
    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user')
        super(CreateProjectForm, self).__init__(*args, **kwargs)
        # self.fields['developer'].choices = [(dev.user.username, dev.user.username) for dev in
        #                                     Developer.objects.exclude(user__username=user).exclude(
        #                                         isProductOwner=True).filter(project=None)]

    project_name = forms.CharField(max_length=30)
    manager = forms.ChoiceField(choices=[(manager, manager) for manager in ScrumMaster.objects.all()])
    # developer = forms.ChoiceField()
    Developer_1 = forms.EmailField(required=False)
    Developer_2 = forms.EmailField(required=False)
    Developer_3 = forms.EmailField(required=False)


class JoinProject(forms.Form):
    def __init__(self, *args, **kwargs):
        project = kwargs.pop('project')
        email = kwargs.pop('email')
        super(JoinProject, self).__init__(*args, **kwargs)
        self.fields['project'].initial = project
        self.fields['email'].initial = email

    project = forms.CharField(widget=forms.HiddenInput())
    email = forms.CharField(widget=forms.HiddenInput())
    login = forms.CharField(max_length=20)
    password = forms.CharField(widget=forms.PasswordInput())
