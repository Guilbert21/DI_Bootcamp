from django.shortcuts import render
from django.http import HttpResponse
import json
import requests


from .models import Animal


def family(request, family_id):
    with open('info/info.json') as f:
        data = json.load(f)

        animals = []
        for animal in data['animals']:
            if animal['family'] == family_id:
                animals.append(animal)

        context = {'animals': animals}
        return render(request, 'info/family.html', context)
    
def animal(requst, animal_id):
    with open('info/info.json') as f:
        data = json.load(f)

        animal = None
        for a in data['animals']:
            if a['id'] == animal_id:
                animal = a

        context = {'animal': animal}
        return render(requests, 'info/animal.html', context)