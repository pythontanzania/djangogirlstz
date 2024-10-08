from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from .forms import SubscriptionForm

class HomePageView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = SubscriptionForm()  # Add subscription form to the context
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

def dar(request):
    form = SubscriptionForm()  
    if request.method == 'POST':
        form = SubscriptionForm(request.POST)
        if form.is_valid():
            form.save()
    return render(request, 'dar.html', {'form': form})

def register(request):
    return render(request, 'register.html')

def login_view(request):
    return render(request, 'login.html')

def subscribe(request):
    form = SubscriptionForm()
    if request.method == 'POST':
        if form.is_valid():
            form.save()
    return redirect('home')  

