from django.db import models

# Create your models here.
class Pooja_Booking(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField()
    pooja_name = models.CharField(50)
    nakshatharam = models.CharField(50)
    date = models.CharField(50)
    quantity = models.IntegerField()
    
    def __str__(self):
        return self.name
    
class Pooja_Info_Table(models.Model):
    pooja_name = models.CharField(max_length=50)
    duration = models.CharField(max_length=15)
    special_note = models.TextField()
    price = models.IntegerField()
    
    def __str__(self) -> str:
        return self.pooja_name
    
class Pooja_Info(models.Model):
    pooja_name = models.CharField(max_length=50)
    nakshatharam = models.CharField(max_length=50)
    
    def __str__(self):
        return self.nakshatharam
    

    
    
    
    

    
    