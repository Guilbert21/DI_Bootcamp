from django.urls import path
from . import views

urlpatterns = [
    path('people', views.people, name='people'),
    path('person/<int:id>', views.person_detail, name='person_detail'),
]