# Generated by Django 3.2.12 on 2022-04-05 08:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_commentaire_titre_commentaire'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commentaire',
            name='titre_commentaire',
            field=models.CharField(max_length=50),
        ),
    ]
