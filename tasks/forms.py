#from django import forms
#from django.contrib.auth.forms import UserCreationForm
#from django.contrib.auth.models import User
from django.forms import ModelForm 
from .models import UserProfile, Baas

class UserProfileForm(ModelForm):
    class Meta:
        model= UserProfile
        fields= ['name', 'lastname', 'username', 'password', 'country', 'phonenumber', 'email', 'accounttype', 'rol', 'description', 'status']


class BaasForm(ModelForm):
    class Meta:
        model= Baas
        fields= ['reportes', 'baas', 'integraciones']



""" class CustomRegisterForm(UserCreationForm):
    name= forms.CharField(max_length=50)
    lastname = forms.CharField(max_length=50)
    username= forms.CharField()
    country= forms.CharField(max_length=50)
    phonenumber= forms.IntegerField()
    email= forms.EmailField()
    accounttype= forms.CharField(max_length=25)
    rol= forms.CharField(max_length=25)
    status=forms.BooleanField()
    description = forms.CharField(max_length=1000)
    

    class Meta:
        model = UserProfile
        fields = ['name', 'lastname', 'username', 'country', 'phonenumber', 'email', 'password1', 'password2', 'accounttype', 'rol', 'description']


 """