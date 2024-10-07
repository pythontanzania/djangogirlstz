from django.shortcuts import render, redirect

from django.views.generic import TemplateView
from .forms import SubscriptionForm

class HomePageView(TemplateView):
    template_name = "index.html"

def community(request):
    return render(request, 'community.html')

def resources(request):
    return render(request, 'resources.html')

def events(request):
    return render(request, 'events.html')

def dar(request):
    return render(request, 'dar.html')

def register(request):
    return render(request, 'register.html')

def login_view(request):
    return render(request, 'login.html')

def subscribe(request):
    if request.method == "POST":
        form = SubscriptionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')  # Redirect to a success page or another page
    else:
        form = SubscriptionForm()
    return render(request, 'subscribe.html', {'form': form})