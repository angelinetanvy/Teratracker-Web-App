# Generated by Django 3.1 on 2020-09-27 02:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('projects', '0012_auto_20200927_0755'),
    ]

    operations = [
        migrations.CreateModel(
            name='TaskStudents',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.IntegerField(default=0)),
                ('student', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('task', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='projects.task')),
            ],
            options={
                'verbose_name': 'Student Tasks',
            },
        ),
        migrations.AddConstraint(
            model_name='taskstudents',
            constraint=models.UniqueConstraint(fields=('student', 'task'), name='unique task student'),
        ),
    ]
