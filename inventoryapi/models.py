from django.db import models

# Create your models here.
class Supplier(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    
class Inventory(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    note = models.TextField()
    stock = models.PositiveIntegerField()
    availability = models.BooleanField(default=False)
    supplier = models.ManyToManyField(Supplier)
        
    def __str__(self):
        return self.name