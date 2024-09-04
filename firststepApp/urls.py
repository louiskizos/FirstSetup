from django.urls import path
from .views import *

app_name="app"
#url, fonction du fichier views, renomme de l'url
urlpatterns=[
    path('',homepage, name='home'),
    path('cours',coursesPages,name='course'),
    path('teacher',TeacherPages,name='teacher'),
    path('test',TestPages,name='test'),
    path('signin',signinPages,name='signin'),
    path('coursdetail',coursesDetails,name='coursdetail'),
    path('mescours',Mescours,name='mescours'),
    path('certificat',certificat,name='certificat'),
    path('module/<int:pk>', modulePage, name='module'),
    path('createuser', createUser, name='createuser'),
    path('login', loginPage, name='login'),
    path('createlogin', createLogin, name='createlogin'),
    path('logout', logout, name='logout'),
    path('createmescours/<int:pk>', createMescours, name='createmescours')
]
