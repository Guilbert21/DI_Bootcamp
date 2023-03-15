from django.shortcuts import render,redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserLoginForm, SignupForm


def signup(request):
    if request.method == 'post':
        form = SignupForm(request.post)
        if form.is_valid():
            user = form.save()
            username = form.clean_data("username")
            password = form.clean_data("password1")
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('films:homepage')
            
    else:
        form = SignupForm()
    return render(request, 'signup.html', {'form': form})

def login_view(request):
    if request.method == 'post':
        form = UserLoginForm(reques=request, data = request)
        if form.is_valid():
            username = form.cleaned_data.get('useranme')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('films:homepage')
    else:
        form = UserLoginForm()
    return render(request, 'login.html', {'form': form})