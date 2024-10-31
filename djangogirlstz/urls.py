from sqlite3 import connect
from django.urls import path
from .views import subscribe
from . import views
from .views import (
    HomePageView,
   
)

urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path('community/', views.community, name='community'),
    path('resources/', views.resources, name='resources'),
    path('events/', views.events, name='events'),
    path('code-of-conduct/', views.code_of_conduct, name='code_of_conduct'),
    path('dar/', views.dar, name='dar'),
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('subscribe/', subscribe, name='subscribe'),
]


