# Generated by Django 4.1 on 2022-08-23 07:02

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='publish',
            field=models.DateTimeField(default=datetime.datetime(2022, 8, 23, 7, 2, 42, 898671, tzinfo=datetime.timezone.utc)),
        ),
    ]