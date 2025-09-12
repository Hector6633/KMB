from django.db import models

# Create your models here.
class PoojaBooking(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField()
    phone_number = models.CharField(max_length=10)
    poojaname = models.CharField(50)
    nak = models.CharField(50)
    booking_date = models.CharField(50)
    quantity = models.IntegerField()
    
    def __str__(self):
        return self.name
    
    
class Pooja_Name(models.Model):
    pooja_name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.pooja_name
    
class Nakshatharam(models.Model):
    nakshatharam = models.CharField(max_length=50)
    
    def __str__(self):
        return self.nakshatharam
    

    
    
    
    

    
    