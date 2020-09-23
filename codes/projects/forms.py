from django import forms
from. import models

class DateInput(forms.DateInput):
    input_type = 'date'

class CreateProjects(forms.ModelForm):
    class Meta:
        model = models.Project
        fields = ['title', 'due_date', 'due_time']
        widgets = {
            'due_date': DateInput()
        }
