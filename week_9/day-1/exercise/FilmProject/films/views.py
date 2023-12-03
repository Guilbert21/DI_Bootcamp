# from django.shortcuts import render
# from .models import Film, Director
# from .forms import FilmForm, DirectorForm
# from django.shortcuts import redirect, timezone


# def homepage(request):
#     film = Film.objects.all()
#     return render(request, 'homepage.html')

# def films(request):
#     film = Film.objects.all()
#     if request.method == 'post':
#         form = FilmForm(request.post)
#         if form.is_valid():
#             form.save()
#             return redirect('homepage')
#     else:
#         form = FilmForm()
#     return render(request, 'films.html', {'film': film, 'form': form})

# def directors(request):
#     if request.method == 'post':
#         form = DirectorForm(request.post)
#         if form.is_valid():
#             form.save()
#             return redirect('homepage')
#     else:
#         form = DirectorForm()
#     return render(request, 'directors.html', {'form': form})

# def film_list(request):
#     films = Film.objects.all()
#     for film in films:
#         film.release_date = film.release_date.strftime("%B %d, %Y")
#     return render(request, 'film_list.html', {'films': films})

from django.shortcuts import render, redirect, get_object_or_404
from .forms import AddFilmForm, AddDirectorForm
from .models import *
from django.urls import reverse
from .forms import AddFilmForm, AddDirectorForm
from django.utils import timezone
from django.contrib.auth.decorators import user_passes_test
from .models import Film, Director
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from .models import Film
from .forms import CommentForm




def addFilm(request):
    form = AddFilmForm()

    if request.method == 'POST':
        form = AddFilmForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('homepage')
        
    context = {
        'form': form
    }
    return render(request, 'add_film.html', context)

def addDirector(request):
    form = AddDirectorForm()

    if request.method == 'POST':
        form = AddDirectorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('homepage')
        
    context = {
        'form': form
    }
    return render(request, 'director/add_director.html', context)

def add_film(request):
    if request.method == 'post':
        form = AddDirectorForm(request.post)
        if form.is_valid():
            title = form.cleaned_data['title']
            release_date = form.cleaned_data['release_date']
            created_in_country = form.cleaned_data['created_in_country']
            available_in_countries = form.cleaned_data['available_in_countries']
            category = form.cleaned_data['category']
            director = form.cleaned_data['director']
            new_film =Film.objects.create(title=title, release_date=release_date, created_in_country=created_in_country, category=category)
            new_film.director.set(director)
            new_film.available_in_countries.set(available_in_countries)
            new_film.save()
            return redirect(reverse('homepage'))
        
    else:
        form = AddFilmForm()
    return render(request, 'add_film.html', {'form': form})

def add_director(request):
    if request.method == 'post':
        form = AddDirectorForm(request.post)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            new_director = Director.objects.create(first_name=first_name, last_name=last_name)
            new_director.save()
            return redirect(reverse('homepage'))
        
    else:
        form = AddDirectorForm()
    return render(request, 'director/add_director.html', {'form': form})

@user_passes_test(lambda u: u.is_superuser)
def delete_film_view(request, film_id):
    film = get_object_or_404(Film, id = film_id)
    film.delete()
    return redirect(reverse('film:homepage'))

@user_passes_test(lambda u: u.is_superuser)
def delete_director_view(request, director_id):
    director = get_object_or_404(Director, id= director_id)
    director.delete()
    return redirect(reverse('film:homepage'))

@login_required
def add_comment(request, film_id):
    film = get_object_or_404(Film, id= film_id)

    if request.method == 'POST':
        form = CommentForm(request.post)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.film = film
            comment.save()
            return redirect('film:film_detail', film_id=film.id)
        
    else:
        form = CommentForm()
    return render(request, 'film/add_comment.html', {'form': form})