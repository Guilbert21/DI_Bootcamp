from django.shortcuts import render
from django import forms

def index(request):
    context = {
        'page_title' : "Homepage",
        'user' : person,
        'form' : ContactForm()
    }
    return render(request, 'posts/homepage.html', context)