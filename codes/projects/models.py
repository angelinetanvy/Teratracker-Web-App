from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=100)
    due_date = models.DateField()
    due_time = models.TimeField()
    supervisor = models.ForeignKey(User, default=None, null=True, on_delete=models.SET_NULL)

    class Meta:
        unique_together = (("title", "supervisor"),)

    def __str__(self):
        return self.title

# Student in Project
class ProjectStudents(models.Model):
    student = models.ForeignKey(User, default=None, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, default=None, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Project Student"
        unique_together = (("student", "project"),)

    def __str__(self):
        return str(self.project) + "-" + str(self.student)
