# Generated by Django 3.1.1 on 2020-09-25 16:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('projects', '0004_auto_20200925_2319'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='students',
        ),
        migrations.CreateModel(
            name='ProjectStudents',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='projects.project')),
                ('student', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('student', 'project')},
            },
        ),
    ]
