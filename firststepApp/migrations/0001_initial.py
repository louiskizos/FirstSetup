# Generated by Django 4.0.1 on 2024-07-22 13:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Adresse',
            fields=[
                ('idAdresse', models.AutoField(primary_key=True, serialize=False)),
                ('pays', models.CharField(max_length=50)),
                ('province', models.CharField(max_length=50)),
                ('commune', models.CharField(max_length=50)),
                ('quartier', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Apprenant',
            fields=[
                ('idApprenant', models.AutoField(primary_key=True, serialize=False)),
                ('nom', models.CharField(max_length=50)),
                ('prenom', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=50)),
                ('telephone', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Cours',
            fields=[
                ('idCours', models.AutoField(primary_key=True, serialize=False)),
                ('designation', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Domaine',
            fields=[
                ('idDomaine', models.AutoField(primary_key=True, serialize=False)),
                ('designation', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Enseignant',
            fields=[
                ('idEnseignant', models.AutoField(primary_key=True, serialize=False)),
                ('nom', models.CharField(max_length=50)),
                ('postnom', models.CharField(max_length=50)),
                ('prenom', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=50)),
                ('telephone', models.CharField(max_length=50)),
                ('adresse', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='firststepApp.adresse')),
            ],
        ),
        migrations.CreateModel(
            name='Module',
            fields=[
                ('idModule', models.AutoField(primary_key=True, serialize=False)),
                ('niveau', models.CharField(max_length=50)),
                ('heures', models.CharField(max_length=50)),
                ('cours', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='firststepApp.cours')),
                ('enseignant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='firststepApp.enseignant')),
            ],
        ),
        migrations.CreateModel(
            name='Participation',
            fields=[
                ('idParticipation', models.AutoField(primary_key=True, serialize=False)),
                ('presences', models.CharField(max_length=50)),
                ('apprenant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='firststepApp.apprenant')),
                ('module', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='firststepApp.module')),
            ],
        ),
        migrations.CreateModel(
            name='Questionnaire',
            fields=[
                ('idQuestionnaire', models.AutoField(primary_key=True, serialize=False)),
                ('designation', models.CharField(max_length=50)),
                ('ponderation', models.IntegerField()),
                ('module', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='firststepApp.module')),
            ],
        ),
        migrations.CreateModel(
            name='Test',
            fields=[
                ('idTest', models.AutoField(primary_key=True, serialize=False)),
                ('points', models.FloatField()),
                ('participation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='firststepApp.participation')),
            ],
        ),
        migrations.CreateModel(
            name='Reponse',
            fields=[
                ('idReponse', models.AutoField(primary_key=True, serialize=False)),
                ('designation', models.CharField(max_length=50)),
                ('questionnaire', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='firststepApp.questionnaire')),
            ],
        ),
        migrations.AddField(
            model_name='cours',
            name='domaine',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='firststepApp.domaine'),
        ),
        migrations.CreateModel(
            name='Contenu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titre', models.CharField(max_length=50)),
                ('video', models.CharField(max_length=50)),
                ('fichier', models.FileField(upload_to='fichier')),
                ('Duree', models.CharField(max_length=50)),
                ('module', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='firststepApp.module')),
            ],
        ),
    ]
