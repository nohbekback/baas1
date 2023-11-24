from django.db import models

class TUser(models.Model):
    name = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    falsename= models.CharField(max_length=50)
    country= models.CharField(max_length=50)
    phonenumber= models.PositiveIntegerField(default=0)
    email= models.EmailField(max_length=150, unique=True)
    password= models.CharField(max_length=100)
    accounttype= models.CharField(max_length=25)
    rol= models.CharField(max_length=25)
    status=models.BooleanField(default=True)
    description = models.TextField()
    createdat = models.DateTimeField(auto_now_add=True)
    updatedat = models.DateTimeField(auto_now=True)
    lastrecord = models.CharField(max_length=50)
class TSession(models.Model):
    user = models.ForeignKey(TUser, on_delete=models.CASCADE)
    idstatus = models.IntegerField()
    idrol = models.IntegerField()
    createdat = models.DateTimeField(auto_now_add=True)
    updatedat = models.DateTimeField(auto_now=True)
    lastrecord = models.CharField(max_length=50)
class TLogin(models.Model):
    user = models.ForeignKey(TUser, on_delete=models.CASCADE)
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
    user = models.ForeignKey(TUser, on_delete=models.CASCADE)
    idsession = models.IntegerField()
    active = models.BooleanField(default=True)
    createdat = models.DateTimeField(auto_now_add=True)
    updatedat = models.DateTimeField(auto_now=True)
    lastrecord = models.CharField(max_length=50)

