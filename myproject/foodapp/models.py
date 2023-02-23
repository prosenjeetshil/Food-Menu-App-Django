from django.db import models

# Create your models here.
class Food(models.Model):
    fname = models.CharField(max_length=30)
    fdesc = models.CharField(max_length=300)
    fprice = models.IntegerField()
    fimg = models.CharField(max_length=300)

    def __str__(self):
        return f'{self.fname}'

# super user - admin
# pass - admin