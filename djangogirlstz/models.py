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
    



    