from django import forms
from . import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _

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

class RemoveStudents(forms.ModelForm):
    class Meta:
        model = models.ProjectStudents
        fields = ['student']

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user')
        super(RemoveStudents, self).__init__(*args, **kwargs)
        self.fields['student'] = forms.ModelChoiceField(queryset=User.objects.filter(is_staff=False))

class CreateTask(forms.ModelForm):
    class Meta:
        model = models.Task
        DIFFICULTY = (
                (1, '1'),
                (2, '2'),
                (3, '3'),
                (4, '4'),
                (5, '5')
                )
        fields = ['taskname', 'taskdesc', 'difficulty', 'start_date', 'start_time', 'due_date', 'due_time', 'task_done']
        difficulty = forms.ChoiceField(widget=forms.Select(choices=DIFFICULTY))
        labels = {
            'taskname': _('Task Name'),
            'taskdesc': _('Task Description'),
            'task_done': _('Done')
        }
        widgets = {
            'start_date': DateInput(),
            'start_time': TimeInput(),
            'due_date': DateInput(),
            'difficulty': forms.Select(choices=DIFFICULTY, attrs={'class': 'form-control'}),
            'due_time': TimeInput()
        }

class AssignMembers(forms.ModelForm):
    class Meta:
        model = models.TaskStudents
        fields = ['student', 'plan_percent']
        labels = {
            'plan_percent': _('Planned Proportion (%)')
        }

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user')
        super(AssignMembers, self).__init__(*args, **kwargs)

    def specify(self, selectedProject, selectedTask):
        project = models.Project.objects.get(title=selectedProject)
        StudentInTaskArray = models.TaskStudents.objects.filter(task=selectedTask).values_list('student_id')
        ProjectStudentsArray = User.objects.filter(pk__in=models.ProjectStudents.objects.filter(project=project).values_list('student_id')).exclude(pk__in=StudentInTaskArray)

        self.fields['student'] = forms.ModelChoiceField(queryset=ProjectStudentsArray)

class DeleteMembers(forms.ModelForm):
    class Meta:
        model = models.TaskStudents
        fields = ['student']

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user')
        super(DeleteMembers, self).__init__(*args, **kwargs)

    def specify(self, selectedProject, selectedTask):
        project = models.Project.objects.get(title=selectedProject)
        StudentInTaskArray = models.TaskStudents.objects.filter(task=selectedTask).values_list('student_id')
        ProjectStudentsArray = User.objects.filter(pk__in=models.ProjectStudents.objects.filter(project=project).values_list('student_id')).filter(pk__in=StudentInTaskArray)

        self.fields['student'] = forms.ModelChoiceField(
            queryset=ProjectStudentsArray)

class AddContribution(forms.ModelForm):
    class Meta:
        labels = {
            'time': _('Time (Hours)')
        }
        model = models.TaskStudents
        fields = ['time']
