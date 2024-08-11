from django.contrib import admin 
from django.urls import path 
from ui import views



urlpatterns = [
    path('login/',views.show ),
]