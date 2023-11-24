from django.shortcuts import render
from django.http import HttpResponse
#importamos funcion q ya tiene django de form
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


# Create your views here.
#home
def home(request):
    return render(request, 'home.html')
#ingresar/registrarse
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
               return HttpResponse('User created successfully')
            except: 
               return HttpResponse('User already exists')#el usuario ya existe
               return HttpResponse ('Password do not match')#contraseñas no coinciden
    
            
