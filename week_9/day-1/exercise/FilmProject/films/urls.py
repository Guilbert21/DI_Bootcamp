from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('homepage', views.homepage),
    path('films', views.films),
    path('directors', views.directors),
    path('film_list', views.film_list),
]