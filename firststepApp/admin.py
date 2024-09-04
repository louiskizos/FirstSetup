from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Adresse)
admin.site.register(Enseignant)
admin.site.register(Apprenant)
admin.site.register(Cours)
admin.site.register(Domaine)
admin.site.register(Module)
admin.site.register(Contenu)
admin.site.register(Participation)
admin.site.register(Test)
admin.site.register(Questionnaire)
admin.site.register(Reponse)