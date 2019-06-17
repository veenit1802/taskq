from django import forms
from .models import TaskModel


class FormSetup(forms.ModelForm):
    class Meta:
        model = TaskModel
        fields = ('name', 'detail')
