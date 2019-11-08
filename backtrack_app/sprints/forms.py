from django import forms
from .models import PBI, SprintBacklog

class SprintForm(forms.Form):
    all_pbi=forms.ModelMultipleChoiceField(queryset=PBI.objects.all(),widget=forms.CheckboxSelectMultiple)

