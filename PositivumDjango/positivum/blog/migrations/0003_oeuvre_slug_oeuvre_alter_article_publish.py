# Generated by Django 4.1 on 2022-08-23 10:38

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_alter_article_publish'),
    ]

    operations = [
        migrations.AddField(
            model_name='oeuvre',
            name='slug_oeuvre',
            field=models.SlugField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='article',
            name='publish',
            field=models.DateTimeField(default=datetime.datetime(2022, 8, 23, 10, 38, 47, 479354, tzinfo=datetime.timezone.utc)),
        ),
    ]