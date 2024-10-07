from django.db import models

# Create your models here.
class Subscription(models.Model):
    email = models.EmailField(unique=True)  # Ensure unique emails
    created_at = models.DateTimeField(auto_now_add=True)  # Track when the subscription was created

    def __str__(self):
        return self.email