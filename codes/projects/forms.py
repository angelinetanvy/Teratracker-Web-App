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
        fields = ['student']

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user')
        super(AssignStudents, self).__init__(*args, **kwargs)
        self.fields['student'] = forms.ModelChoiceField(queryset=User.objects.filter(is_staff=False))

class CreateTask(forms.ModelForm):
    class Meta:
        model = models.Task
        fields = ['taskname', 'taskdesc', 'taskdone']

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

        