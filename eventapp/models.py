from django.db import models

# Create your models here.
class Event(models.Model):
    image = models.ImageField(upload_to='media')
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=100)
    
    #to show the name in the database column as string
    def __str__(self):
        return self.name
    
class Booking(models.Model):
    customerName = models.CharField(max_length=50)
    customerPhone = models.CharField(max_length=12)
    #need name of the event
    name = models.ForeignKey(Event, on_delete=models.CASCADE)
    bookingDate = models.DateField()
    bookedAt =  models.DateField(auto_now=True)
    