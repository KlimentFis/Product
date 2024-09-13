from django.db import models

# Create your models here.
class Product():
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    price = models.IntegerField()


