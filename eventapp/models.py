from django.db import models

# Create your models here.
class Event(models.Model):
    image = models.ImageField(upload_to='media')
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=100)