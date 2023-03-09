from django.db import models

# Create your models here.
class Store(models.Model):
   username = models.CharField(max_length=255)
   email = models.CharField(max_length=255)
   phone = models.CharField(max_length=2500)
   bookname = models.CharField(max_length=250000)
   Authorname = models.CharField(max_length=2500)