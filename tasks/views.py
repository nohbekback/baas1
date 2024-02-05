from django.shortcuts import render, redirect
from django.http import HttpResponse
#importamos funcion q ya tiene django de form
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate  # crea la cookie
from django.db import IntegrityError  # error excepcional
from .models import UserProfile
from .forms import UserProfileForm, BaasForm


# Create your views here.
#home
def home(request):
    return render(request, 'home.html')
#ingresar/registrarse
# register2 // NO CONECTA A LA BBDD
def register(request):
    if request.method == 'POST': #ESTABA CON POST
        form = UserProfileForm(request.POST) #ESTABA CON POST
        if form.is_valid():
            user: form.save()
            user_profile = UserProfile(user=user) #la variable user me da error 
            user_profile.save()
            return redirect('home')
    else:
        form = UserProfileForm()
    return render(request, 'register.html', {
        'form': form
        })  

# registrarse// CON ESTE SE REGISTRA OK Y CONECTA CON LA BBDD
def signup(request):
    if request.method == 'GET':
        #form que nos facilita django
        return render(request, 'signup.html',{
        'form':UserCreationForm
    })
    else:
        #compara las contraseñas
        if request.POST['password1'] == request.POST['password2']:
            try: #creamos el usuario, con una consulta a la bbdd
               user = User.objects.create_user(username = request.POST['username'],
               password = request.POST['password1'])
               user.save() #guarda el usuario creado
               login(request, user) #crea la cookie
               return redirect('tasks')
            except IntegrityError: #excepciones de error especifico
               return render(request, 'signup.html',{
                   'form':UserCreationForm,
                   'error':'User already exists'
             })#el usuario ya existe
        return render(request, 'signup.html',{
             'form':UserCreationForm,
            'error':'Password do not match'#contraseñas no coinciden
        })

# tareas
def tasks(request):
    return render(request, 'tasks.html')

#serviciosBaas
def serviciosBaas(request):
    if request.method == 'GET':
     return render(request, 'serviciosBaas.html',{
        'form': BaasForm
    })
    else:
        print(request.POST)
        return render(request, 'serviciosBaas.html',{
        'form': BaasForm
    })

# cierre de sesion
def signout(request):
    logout(request)
    return redirect('home')

# login
def signin(request):
    if request.method == 'GET':
        return render(request, 'signin.html', {
            'form': AuthenticationForm
        })
    else:  # validar usuario
       user = authenticate(
           request, username=request.POST['username'], password=request.POST['password'])
       if user is None:  # si el usuario no esta correcto o en blanco
           return render(request, 'signin.html', {
               'form': AuthenticationForm,
               'error': 'Username or password is incorrect'
           })
       else:
        login(request, user)
        return redirect('tasks')

