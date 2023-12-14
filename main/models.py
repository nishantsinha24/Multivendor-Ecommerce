from django.db import models
from django.contrib.auth.models import User

# User models here.
class Vendor(models.Model):
    user = models.ForeignKey(User , on_delete=models.CASCADE)
    address = models.TextField(null=True)
    
class ProductCategory(models.Model):
    title = models.CharField(max_length=200)
    detail = models.TextField(null=True)
    
    def __str__(self) :
        return self.title
    
class Product(models.Model):
    title = models.CharField(max_length=200)
    details = models.TextField(null=True)
    price = models.FloatField()
    
    def __str_(self):
        return self.title
            
     
