from django import forms
from. import models
from django.contrib.auth.models import User

class DateInput(forms.DateInput):
    input_type = 'date'

class CreateProjects(forms.ModelForm):
    class Meta:
        model = models.Project
        fields = ['title', 'due_date', 'due_time']
        students = forms.ModelChoiceField(queryset=User.objects.all())
        widgets = {
            'due_date': DateInput()
        }
