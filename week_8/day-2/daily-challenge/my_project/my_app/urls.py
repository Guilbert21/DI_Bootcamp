from django.contrib import admin
from django.urls import path
from . import views

# Create a view /persons/phonenumber that will display all the info of a person depending on his phone number



urlpatterns = [
    path('persons/phonenumber/<str:phone_number>/', views.person_by_phone_number, name = 'person_by_phone_number'),
    path('persons/name/<str:name>/', views.person_by_name, name='person_by_name'),
]
