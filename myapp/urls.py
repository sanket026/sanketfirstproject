from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
    path('',views.index),
    path('notes/',views.notes,name="notes"),
    path('userlogout/',views.userlogout),
    path('profile/',views.profile),
    path('about/',views.about),
    path('contact/',views.contact),
   
    
    
]
