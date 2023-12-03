from django.shortcuts import render,redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .forms import SignupForm, LoginForm

def signup_view(request):
    if request.method == 'post':
        form = SignupForm(request.post)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('homepage')
        
    else:
        form = SignupForm()
    return render(request, 'signup.html', {'form': form})

def login_view(request):
    if request.method == 'post':
        form = LoginForm(request.post)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            return redirect('homepage')
        
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('homepage')

@login_required
def profile_view(request):
    user = user.objects.get(id  = user_id)
    return render(request, 'profile.html', {'user': user})