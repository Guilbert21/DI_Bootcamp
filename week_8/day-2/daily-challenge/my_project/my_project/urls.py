"""my_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views

# Create a view /persons/phonenumber that will display all the info of a person depending on his phone number



urlpatterns = [
    path('persons/phonenumber/<str:phone_number>/', views.person_by_phone_number, name = 'person_by_phone_number'),
    path('persons/name/<str:name>/', views.person_by_name, name='person_by_name'),
]
