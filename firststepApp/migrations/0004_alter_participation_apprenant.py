# Generated by Django 4.0.1 on 2024-07-23 12:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('firststepApp', '0003_cours_duree_cours_image_cours_prix'),
    ]

    operations = [
        migrations.AlterField(
            model_name='participation',
            name='apprenant',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
