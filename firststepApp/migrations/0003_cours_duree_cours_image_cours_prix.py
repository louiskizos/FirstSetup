# Generated by Django 4.0.1 on 2024-07-23 07:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firststepApp', '0002_enseignant_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='cours',
            name='duree',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='cours',
            name='image',
            field=models.ImageField(null=True, upload_to='cours'),
        ),
        migrations.AddField(
            model_name='cours',
            name='prix',
            field=models.IntegerField(default=120),
        ),
    ]
