from django import forms
from .models import Subscription
from .models import User

class SubscriptionForm(forms.ModelForm):
    class Meta:
        model = Subscription
        fields = ['email']
        widgets = {
            'email': forms.EmailInput(attrs={'placeholder': 'Enter your email', 'class': 'form-control'})
        }


class UserRegistrationForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['school_email', 'full_name', 'phone_number', 'password']

    # Custom clean method to handle password validation (if needed)
    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        # Add any password validation logic here if needed
        return cleaned_data

class LoginForm(forms.Form):
    email = forms.EmailField(label='Email', max_length=254)
    password = forms.CharField(label='Password', widget=forms.PasswordInput)