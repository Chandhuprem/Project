from django.db import models

# Create your models here.
class MyModel(models.Model):
   bname = models.CharField(max_length=255)
   bprice = models.FloatField()
   author = models.CharField(max_length=2500)
   story = models.CharField(max_length=250000)
   image = models.CharField(max_length=2500)
class Newbook(models.Model):
   images = models.CharField(max_length=2500)
   
      


