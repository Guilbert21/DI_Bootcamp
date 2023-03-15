from django.shortcuts import render
from .models import Film, Director
from .forms import FilmForm, DirectorForm
from django.shortcuts import redirect, timezone


def homepage(request):
    film = Film.objects.all()
    return render(request, 'homepage.html')

def films(request):
    film = Film.objects.all()
    if request.method == 'post':
        form = FilmForm(request.post)
        if form.is_valid():
            form.save()
            return redirect('homepage')
    else:
        form = FilmForm()
    return render(request, 'films.html', {'film': film, 'form': form})

def directors(request):
    if request.method == 'post':
        form = DirectorForm(request.post)
        if form.is_valid():
            form.save()
            return redirect('homepage')
    else:
        form = DirectorForm()
    return render(request, 'directors.html', {'form': form})

def film_list(request):
    films = Film.objects.all()
    for film in films:
        film.release_date = film.release_date.strftime("%B %d, %Y")
    return render(request, 'film_list.html', {'films': films})