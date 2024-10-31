from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.views.generic import TemplateView
from .forms import SubscriptionForm 
from .forms import UserRegistrationForm
from .forms import LoginForm

class HomePageView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = SubscriptionForm()  
        return context

def community(request):
    form = SubscriptionForm()
    if request.method == 'POST':
        form = SubscriptionForm(request.POST)
        if form.is_valid():
            form.save()
    return render(request, 'community.html', {'form': form})

def resources(request):
    form = SubscriptionForm()
    if request.method == 'POST':
        form = SubscriptionForm(request.POST)
        if form.is_valid():
            form.save()
    return render(request, 'resources.html', {'form': form})

def events(request):
    form = SubscriptionForm()
    if request.method == 'POST':
        form = SubscriptionForm(request.POST)
        if form.is_valid():
            form.save()
    return render(request, 'events.html', {'form': form})

def code_of_conduct(request):
    form = SubscriptionForm()
    if request.method == 'POST':
        form = SubscriptionForm(request.POST)
        if form.is_valid():
            form.save()
    return render(request, 'code_of_conduct.html', {'form': form})

def dar(request):
    form = SubscriptionForm()  
    if request.method == 'POST':
        form = SubscriptionForm(request.POST)
        if form.is_valid():
            form.save()
    return render(request, 'dar.html', {'form': form})

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')  
    else:
        form = UserRegistrationForm()
    return render(request, 'register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            # Use email for username if you have set up User model accordingly
            user = authenticate(request, username=email, password=password)

            if user is not None:
                login(request, user)
                return redirect('home')  # Redirect to the home page or dashboard
            else:
                form.add_error(None, "Invalid email or password.")
    else:
        form = LoginForm()
    
    return render(request, 'login.html', {'form': form})

def subscribe(request):
    form = SubscriptionForm()
    if request.method == 'POST':
        if form.is_valid():
            form.save()
    return redirect('home')  

