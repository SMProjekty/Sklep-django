from django.db import models

# Create your models here.

class User(models.Model):
    UserId = models.AutoField(primary_key=True)
    Email = models.EmailField(max_length=25, unique=True)
    Pass = models.CharField(max_length=30)

class Shop(models.Model):
    ShopId = models.AutoField(primary_key=True)
    UserId = models.IntegerField(default=None)
    NameShop = models.CharField(max_length=25)

class Product(models.Model):
    ProductId = models.AutoField(primary_key=True)
    ShopId = models.IntegerField(default=None)
    NameProduct = models.CharField(max_length=25)
    ActivProduct = models.CharField(max_length=2)