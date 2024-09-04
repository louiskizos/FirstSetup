from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Adresse(models.Model):
    idAdresse = models.AutoField(primary_key=True)
    pays = models.CharField(max_length=50)
    province = models.CharField(max_length=50)
    commune = models.CharField(max_length=50)
    quartier = models.CharField(max_length=50)

class Enseignant(models.Model):
    idEnseignant = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=50)
    postnom = models.CharField(max_length=50)
    prenom = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    telephone = models.CharField(max_length=50)
    image = models.ImageField(upload_to='enseignant', null=True)
    adresse = models.ForeignKey(Adresse, on_delete=models.CASCADE)

class Apprenant(models.Model):
    idApprenant = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=50)
    prenom = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    telephone = models.CharField(max_length=50)

class Domaine(models.Model):
    idDomaine = models.AutoField(primary_key=True)
    designation = models.CharField(max_length=50)

class Cours(models.Model):
    idCours = models.AutoField(primary_key=True)
    designation = models.CharField(max_length=50)
    domaine = models.ForeignKey(Domaine, on_delete=models.CASCADE)
    prix = models.IntegerField(default=120)
    duree = models.IntegerField(default=1)
    image = models.ImageField(upload_to='cours', null=True)

class Module(models.Model):
    idModule = models.AutoField(primary_key=True)
    niveau = models.CharField(max_length=50)
    heures = models.CharField(max_length=50)
    enseignant = models.ForeignKey(Enseignant, on_delete=models.CASCADE)
    cours = models.ForeignKey(Cours, on_delete=models.CASCADE)

class Contenu(models.Model):
    titre = models.CharField(max_length=50)
    video = models.CharField(max_length=50)
    fichier = models.FileField(upload_to='fichier')
    Duree = models.CharField(max_length=50)
    module = models.ForeignKey(Module, on_delete=models.CASCADE)

class Participation(models.Model):
    idParticipation = models.AutoField(primary_key=True)
    apprenant = models.IntegerField()
    module = models.ForeignKey(Module, on_delete=models.CASCADE)

class Test(models.Model):
    idTest = models.AutoField(primary_key=True)
    participation = models.ForeignKey(Participation, on_delete=models.CASCADE)
    points = models.FloatField()

class Questionnaire(models.Model):
    idQuestionnaire = models.AutoField(primary_key=True)
    designation = models.CharField(max_length=50)
    ponderation = models.IntegerField()
    module = models.ForeignKey(Module, on_delete=models.CASCADE)

class Reponse(models.Model):
    idReponse = models.AutoField(primary_key=True)
    designation = models.CharField(max_length=50)
    questionnaire = models.ForeignKey(Questionnaire, on_delete=models.CASCADE)