from django.contrib import admin
from django.urls import path
from . import views, delete_film_view

app_name = 'films'

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('homepage', views.homepage, name='homepage'),
    # path('films', views.films),
    # path('directors', views.directors),
    path('add-film/', views.addFilm, name='add-film'),
    path('add-director/', views.addDirector, name='add-director'),
    path('addFilm/', views.add_film, name='add_film'),
    path('addDirector/', views.add_director, name='add_director'),
    path('films/<int:id>/', delete_film_view.delete_film, name='delete_film'),
    path('films/<int:film_id>/add_comment/', views.add_comment, name='add_comment'),
]