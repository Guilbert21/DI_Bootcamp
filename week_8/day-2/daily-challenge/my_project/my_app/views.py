from django.shortcuts import render
from django.http import HttpResponse
from .models import Person

def person_by_phone_number(request, phone_number):
    try:
        person = Person.objects.get(phone_number=phone_number)
        context = {'person': person}
        return render(request, 'person.html', context)
    
    except Person.DoesNotExist:
        return HttpResponse('Person does not exist')
    

def person_by_name(request, name):
    persons = Person.object.filter(name__icontains=name)
    if persons.exists():
        context = {'persons': persons}
        return render(request, 'persons.html', context)
    else:
        return HttpResponse('Person does not exist')

# Create your views here.
