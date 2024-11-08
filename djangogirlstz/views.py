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
            'bio': 'Catherine Rose is dedicated to building an inclusive ecosystem that empowers everyone through skill development and collaboration.',
            'image': 'djangogirlstz/images/c-catherinerose.png'
        },
        {
            'name': 'Noah',
            'role': 'Patron',
            'bio': 'Noah combines his passion for engineering and development with his love for swimming, making a splash in both fields!',
            'image': 'djangogirlstz/images/c-noah.png'
        },
        {
            'name': 'Lupyana',
            'role': 'Software Developer',
            'bio': 'He’s still thinking of a fun fact to share!',
            'image': 'djangogirlstz/images/lupyana.png'
        },
        {
            'name': 'Fuad',
            'role': 'Systems Engineer',
            'bio': 'When he’s not engineering systems, Fuad is honing his skills as a professional pool table player.',
            'image': 'djangogirlstz/images/fuad.png'  
        },
        {
            'name': 'Glory',
            'role': 'Chapter Lead - Ardhi University',
            'bio': 'Glory loves turning imaginative ideas into reality through her passion for technology.',
            'image': 'djangogirlstz/images/Glory.jpeg'  
        },
        {
            'name': 'Sabrina',
            'role': 'Developer',
            'bio': 'Sabrina is a team player and a developer who thrives both in collaboration and independent work!',
            'image': 'djangogirlstz/images/team.jpeg'  
        },
        {
            'name': 'Thecla',
            'role': 'Chapter Lead - UDSM',
            'bio': 'Thecla brings the perfect mix of fun and focus—she’s dedicated to her work but knows how to keep things lively',
            'image': 'djangogirlstz/images/Thecla.jpeg'  
        },
        {
            'name': 'Basilisa',
            'role': 'Chapter Lead - DIT',
            'bio': 'Basilisa ensures that projects run smoothly and on time.',
            'image': 'djangogirlstz/images/Basilisa.jpeg' 
        },
        {
            'name': 'Hajra',
            'role': 'Chapter Mentor',
            'bio': 'Hajra’s dedication and drive inspire others on their tech journeys. She’s always ready to lend a helping hand and share her passion for learning',
            'image': 'djangogirlstz/images/team.jpeg' 
        },
        {
            'name': 'Zubeda',
            'role': 'Chapter Lead - Mzumbe/Developer',
            'bio': 'Zubeda is a dedicated soul with infectious energy, bringing a unique charm that brightens the team!',
            'image': 'djangogirlstz/images/Zubeda.jpeg' 
        },
        {
            'name': 'Debora',
            'role': 'Developer',
            'bio': 'Debora is a very curious thinker with a logical mind who loves to learn.',
            'image': 'djangogirlstz/images/Debrah.jpeg' 
        },
        
    ]

    context = {
        'team_members': team_members
    }
    return render(request, 'about.html', context)