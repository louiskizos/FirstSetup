from django.shortcuts import render,redirect
from django.contrib.auth.models import User, auth
from .models import *

# Create your views here.
def loginPage(request):
    page='login.html'
    return render(request, page)

def logout(request):
    auth.logout(request)
    return redirect('app:home')

def createLogin(request):
    if request.method=='POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = auth.authenticate(username=username, password=password)
        
        if user is not None:
            auth.login(request, user)
            return redirect('app:home')
        else:
            message_erreur = "Desole veuillez renseigner les champs"
            return render(request, 'login.html', {'message_erreur':message_erreur})

# register
def createUser(request):
    if request.method=='POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        if User.objects.filter(email=email).exists():
            message_erreur = "L'utilisateur existe deja"
            return render(request, 'signin.html', {'message_erreur':message_erreur})
        else:
            formulaire = User(
                username=username,
                password=password,
                email=email
            )
            formulaire.set_password(password)
            formulaire.save()
            return redirect('app:login')
# fin fin
def homepage(request):
    page='index.html'
    return render(request,page)

def coursesPages(request):
    cours = Cours.objects.select_related('domaine')
    context = {
        'cours':cours
    }
    page='cours.html'
    return render(request,page, context)

def TeacherPages(request):
    enseignant = Enseignant.objects.all()
    context = {
        'enseignant':enseignant
    }
    page='enseignant.html'
    return render(request,page, context)

def TestPages(request):
    page='test.html'
    return render(request,page)

def signinPages(request):
    page='signin.html'
    return render(request,page)

def coursesDetails(request):
    page='course_details.html'
    return render(request,page)

def Mescours(request):
    if request.user.is_authenticated:
        user_id = request.user.id
        participation = Participation.objects.select_related('module').filter(apprenant=user_id)
        context = {
            'participation': participation
        }
        page='mescours.html'
        return render(request, page, context)

def createMescours(request, pk):
    if request.user.is_authenticated:
        user_id = request.user.id
        user = User.objects.get(id=user_id)
        module = Module.objects.get(idModule=pk)
        module.idModule
        
        formulaire = Participation(
            apprenant=user_id,
            module=module
        )
        formulaire.save()
        return redirect('app:home')

def certificat(request):
    page='certificat.html'
    return render(request,page)

def modulePage(request, pk):
    module = Module.objects.select_related('enseignant', 'cours').filter(cours=pk)
    context = {
        'module':module
    }
    page='module.html'
    return render(request,page, context)
    