from django.db import models
from django.contrib.auth.models import User 


class UserProfile(models.Model):
    name = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    USERNAME_FIELD = 'username'
    username= models.CharField(max_length=50)
    country= models.CharField(max_length=50)
    phonenumber= models.PositiveIntegerField(default=0)
    email= models.EmailField('email address', unique=True)
    password= models.CharField(max_length=100)
    accounttype= models.CharField(max_length=25)
    rol= models.CharField(max_length=25)
    status=models.BooleanField(default=True)
    description = models.TextField(max_length=1000)
    createdat = models.DateTimeField(auto_now_add=True)
    updatedat = models.DateTimeField(auto_now=True)
    lastrecord = models.CharField(max_length=50) 

    def __str__(self):
      return f"{self.user.username} - {self.user.email}"
    #El método __str__ que se define en el modelo UserProfile es utilizado para proporcionar una representación legible de los objetos de ese modelo. 
    
class Baas(models.Model):
    reportes= models.TextField(max_length=1000)
    baas= models.TextField(max_length=1000)
    integraciones= models.TextField(max_length=1000)

class TSession(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    idstatus = models.IntegerField()
    idrol = models.IntegerField()
    createdat = models.DateTimeField(auto_now_add=True)
    updatedat = models.DateTimeField(auto_now=True)
    lastrecord = models.CharField(max_length=50)
class TLogin(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    idstatus = models.IntegerField()
    rol= models.CharField(max_length=25)
    active = models.BooleanField(default=True)
    createdat = models.DateTimeField(auto_now_add=True)
    updatedat = models.DateTimeField(auto_now=True)
    lastrecord = models.CharField(max_length=50)
class AccountType(models.Model):
    name = models.CharField(max_length=50)
    active = models.BooleanField(default=True)
class Rol(models.Model):
    idrol = models.IntegerField()
class Status(models.Model):
    idstatus = models.IntegerField()
class SessionHistory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    idsession = models.IntegerField()
    active = models.BooleanField(default=True)
    createdat = models.DateTimeField(auto_now_add=True)
    updatedat = models.DateTimeField(auto_now=True)
    lastrecord = models.CharField(max_length=50)



# Create your models here.
