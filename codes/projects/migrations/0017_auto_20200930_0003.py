# Generated by Django 3.1.1 on 2020-09-29 17:03

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0016_auto_20200930_0002'),
    ]

    operations = [
        migrations.AlterField(
            model_name='taskstudents',
            name='time',
            field=models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(2), django.core.validators.MaxValueValidator(100)]),
        ),
    ]
