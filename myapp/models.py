
from django.db import models

# Create your models here.

class usersignup(models.Model):
    firstname=models.CharField(max_length=20)
    lastname=models.CharField(max_length=20)
    password=models.CharField(max_length=20)
    username=models.CharField(max_length=20)
    state=models.CharField(max_length=20)
    city=models.CharField(max_length=20)
    zipcode=models.IntegerField()

class notesdata(models.Model):
    title=models.CharField(max_length=100)
    opt=models.CharField(max_length=100)
    myfile=models.FileField(upload_to="notesupload")
    comments=models.TextField()    

class contactdata(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField()
    phonenum=models.BigIntegerField()
    msg=models.CharField(max_length=200)