from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=100, unique=True)
    due_date = models.DateField()
    due_time = models.TimeField()
    supervisor = models.ForeignKey(User, default=None, null=True, on_delete=models.SET_NULL)
    students = models.ForeignKey(User, default=None, null=True, on_delete=models.SET_NULL, related_name="students")
    # tasks =
