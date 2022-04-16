from django.db import models
import uuid

# Create your models here.

class Tour(models.Model):
    location = models.CharField(max_length=200, blank=True, null=True)
    date = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.location

class Booking(models.Model):
    customer = models.CharField(max_length=50)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    charge = models.IntegerField(default=0, null=True, blank=True)
    email = models.EmailField(max_length=500, blank=True, null=True)
    tour = models.ForeignKey(Tour,on_delete=models.CASCADE,null=True) 
    
    def __str__(self):
        return self.customer



