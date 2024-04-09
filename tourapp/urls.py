from django.urls import path
from . import views

urlpatterns = [
     path('register',views.register,name="register"),
    path('login',views.login,name="login"),
    path('index',views.index,name="index"),
     path('',views.base,name="base"),
     path('about',views.about,name="about"),
     path('contact',views.contact,name="contact"),
       path('services',views.services,name="services"),
]