from django.db import models

# Create your models here.
class bookTable(models.Model):
    Tname=models.CharField(max_length=100)
    Temail=models.EmailField(max_length=254)
    Tphone=models.TextField(max_length=100)
    Tdate = models.DateField()
    Ttime = models.TimeField()
    Tpeople=models.TextField(max_length=100)
    Tmessage=models.TextField(max_length=100)
    

class ContactUS(models.Model):
    ContactName=models.CharField(max_length=100)
    ContactEmail=models.EmailField(max_length=254)
    subject=models.TextField(max_length=100)
    ContactMessage=models.TextField(max_length=100)

class SubEmail(models.Model):
    email=models.EmailField(max_length=254)