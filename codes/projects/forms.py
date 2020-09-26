from django import forms
from . import models
from django.contrib.auth.models import User

class DateInput(forms.DateInput):
    input_type = 'date'


class CreateProjects(forms.ModelForm):
    class Meta:
        model = models.Project
        fields = ['title', 'due_date', 'due_time']
        widgets = {
            'due_date': DateInput()
        }

class AssignStudents(forms.ModelForm):
    class Meta:
        model = models.ProjectStudents
        fields = ['project', 'student']

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user')
        super(AssignStudents, self).__init__(*args, **kwargs)
        self.fields['project'] = forms.ModelChoiceField(queryset=models.Project.objects.filter(supervisor=user))
        self.fields['student'] = forms.ModelChoiceField(queryset=User.objects.filter(is_staff=False))
