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

# def about(request):
#     form = SubscriptionForm()
#     if request.method == 'POST':
#         form = SubscriptionForm(request.POST)
#         if form.is_valid():
#             form.save()
#     return render(request, 'about.html', {'form': form})
def code_of_conduct(request):
    return render(request, 'code_of_conduct.html')

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

def about(request):
    team_members = [
        {
            'name': 'CatherineRose',
            'role': 'Convener',
            'bio': 'Building inclusive ecosystem focused oon skill development',
            'image': 'djangogirlstz/images/c-catherinerose.png'
        },
        {
            'name': 'Noah',
            'role': 'Patron',
            'bio': 'Engineering development and swimming',
            'image': 'djangogirlstz/images/c-noah.png'
        },
        {
            'name': 'Lupyana',
            'role': 'Software Developer',
            'bio': 'He does not have a fun fact',
            'image': 'djangogirlstz/images/lupyana.png'
        },
        {
            'name': 'Fuad',
            'role': 'Systems Engineer',
            'bio': 'Fuad is a professional pool table player.',
            'image': 'djangogirlstz/images/fuad.png'  
        },
        {
            'name': 'Glory',
            'role': 'Tech Enthusiast',
            'bio': 'Glory loves to implement things that are imaginable.',
            'image': 'djangogirlstz/images/team.jpeg'  
        },
        {
            'name': 'Sabrina',
            'role': 'Developer',
            'bio': 'Sabrina enjoys working with data and uncovering insights.',
            'image': 'djangogirlstz/images/team.jpeg'  
        },
        {
            'name': 'Thecla',
            'role': 'Tech Enthusiast',
            'bio': 'Thecla is dedicated to designing user-friendly interfaces.',
            'image': 'djangogirlstz/images/team.jpeg'  
        },
        {
            'name': 'Basilisa',
            'role': 'Tech Enthusiast',
            'bio': 'Basilisa ensures that projects run smoothly and on time.',
            'image': 'djangogirlstz/images/team.jpeg' 
        },
        {
            'name': 'Hajra',
            'role': 'Tech Enthusiast',
            'bio': 'Hajra focuses on maintaining high quality in all our projects.',
            'image': 'djangogirlstz/images/team.jpeg' 
        },
        {
            'name': 'Zubeda',
            'role': 'Developer',
            'bio': 'Zubeda crafts engaging content for our community.',
            'image': 'djangogirlstz/images/team.jpeg' 
        },
        {
            'name': 'Debora',
            'role': 'Developer',
            'bio': 'Debora is skilled in promoting our initiatives and reaching more women.',
            'image': 'djangogirlstz/images/team.jpeg' 
        },
        
    ]

    context = {
        'team_members': team_members
    }
    return render(request, 'about.html', context)