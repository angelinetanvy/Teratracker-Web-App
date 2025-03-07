# Generated by Django 3.1.1 on 2020-09-25 16:19

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('projects', '0003_auto_20200925_2142'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='students',
            field=models.ManyToManyField(related_name='Students', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterUniqueTogether(
            name='project',
            unique_together=set(),
        ),
        migrations.DeleteModel(
            name='ProjectStudents',
        ),
    ]
