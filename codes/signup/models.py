from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=200, help_text='User Name')

    def __str__(self):
        return self.name

