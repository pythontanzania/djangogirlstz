from django.db import models

# Create your models here.
class Subscription(models.Model):
    email = models.EmailField(unique=True)  
    created_at = models.DateTimeField(auto_now_add=True) 

    def __str__(self):
        return self.email
    
class User(models.Model):
    school_email = models.EmailField(unique=True)
    full_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    password = models.CharField(max_length=128)  # Use a hashed password in practice
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.full_name
    

from django.db import models

class Event(models.Model):
    title = models.CharField(max_length=255)
    date = models.DateField()
    time = models.CharField(max_length=50)
    location = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='events/', null=True, blank=True)

    def __str__(self):
        return self.title


    