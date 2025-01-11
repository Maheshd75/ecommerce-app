from django.db import models

# Create your models here.

class Products(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    price = models.IntegerField(default=0)
    image = models.CharField(max_length=200)
    category = models.CharField(max_length=200)
    subCategory = models.CharField(max_length=200)
    
   