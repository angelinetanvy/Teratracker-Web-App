from django import forms
from . import models
from django.contrib.auth.models import User

class DateInput(forms.DateInput):
    input_type = 'date'

class TimeInput(forms.TimeInput):
    input_type = 'time'

class CreateProjects(forms.ModelForm):
    class Meta:
        model = models.Project
        fields = ['title', 'due_date', 'due_time']
        widgets = {
            'due_date': DateInput(),
            'due_time': TimeInput()
        }

class AssignStudents(forms.ModelForm):
    class Meta:
        model = models.ProjectStudents
        fields = ['student']

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user')
        super(AssignStudents, self).__init__(*args, **kwargs)
        self.fields['student'] = forms.ModelChoiceField(queryset=User.objects.filter(is_staff=False))

class CreateTask(forms.ModelForm):
    class Meta:
        model = models.Task
        fields = ['taskname', 'taskdesc', 'start_date', 'start_time', 'due_date', 'due_time', 'task_done']
        widgets = {
            'start_date': DateInput(),
            'start_time': TimeInput(),
            'due_date': DateInput(),
            'due_time': TimeInput()
        }

class AssignMembers(forms.ModelForm):
    class Meta:
        model = models.TaskStudents
        fields = ['student', 'time']

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user')
        super(AssignMembers, self).__init__(*args, **kwargs)

    def specify(self, selectedTask, selectedProject):
        project = models.Project.objects.get(title=selectedProject)
        self.fields['student'] = forms.ModelChoiceField(queryset=User.objects.filter(pk__in=models.ProjectStudents.objects.filter(project=project).values_list('student_id')))

        