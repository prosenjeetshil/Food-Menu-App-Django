from django.db import models

# Create your models here.
class Food(models.Model):
    fid = models.IntegerField()
    fname = models.CharField(max_length=30)
    fdesc = models.CharField(max_length=150)
    fprice = models.IntegerField()