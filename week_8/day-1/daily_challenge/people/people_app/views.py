from django.shortcuts import render
from .models import Person

people = [
  {
    'id': 1,
    'name': 'Bob Smith',
    'age': 35,
    'country': 'USA'
  },
  {
    'id': 2,
    'name': 'Martha Smith',
    'age': 60,
    'country': 'USA'
  },
  {
    'id': 3,
    'name': 'Fabio Alberto',
    'age': 18,
    'country': 'Italy'
  },
  {
    'id': 4,
    'name': 'Dietrich Stein',
    'age': 85,
    'country': 'Germany'
  }
]



def people(request):
    people_list = Person.objects.all().order_by('age')
    return render(request, 'people.html', {'people_list':people_list})

def person_detail(request, id):
    person = Person.objects.get(id=id)
    return render(request, 'person_detail.html', {'person':person})