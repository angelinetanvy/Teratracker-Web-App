from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=100)
    due_date = models.DateField()
    due_time = models.TimeField()
    supervisor = models.ForeignKey(User, default=None, on_delete=models.SET_DEFAULT)

    class Meta:
        constraints = [models.UniqueConstraint(fields=['title', 'supervisor'], name="unique title")]
        verbose_name = "Project"

    def __str__(self):
        return str(self.title) + "-" + str(self.supervisor)

# Student in Project
class ProjectStudents(models.Model):
    student = models.ForeignKey(User, default=None, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, default=None, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Project Student"
        constraints = [models.UniqueConstraint(fields=['student', 'project'], name="unique project student")]

    def __str__(self):
        return str(self.project) + "-" + str(self.student)
