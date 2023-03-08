from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    context = {
        'posts': posts
}
    

def about(request):
    return HttpResponse('<h1>Blog About</h1>')

