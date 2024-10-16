from django.contrib import admin
from .models import User, Subscription  

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('school_email', 'full_name', 'phone_number', 'created_at')  
    search_fields = ('school_email', 'full_name')  
    list_filter = ('created_at',)  
    ordering = ('-created_at',)  

@admin.register(Subscription)
class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ('email', 'created_at')  
    search_fields = ('email',)  
    list_filter = ('created_at',)  
    ordering = ('-created_at',)  
