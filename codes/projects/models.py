from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=100)
    due_date = models.DateField()
    due_time = models.TimeField()
    supervisor = models.ForeignKey(settings.AUTH_USER_MODEL, default=None, null=True, on_delete=models.SET_NULL)
    # tasks =
