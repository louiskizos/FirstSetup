# Generated by Django 4.0.1 on 2024-07-22 13:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firststepApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='enseignant',
            name='image',
            field=models.ImageField(null=True, upload_to='enseignant'),
        ),
    ]
