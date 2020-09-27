from django.contrib import admin
from .models import Project, ProjectStudents, Task, TaskStudents

# Register your models here.
admin.site.register(Project)
admin.site.register(ProjectStudents)
admin.site.register(Task)
admin.site.register(TaskStudents)
