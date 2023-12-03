from django.urls import path
from .views import home, about, RoomList

urlpatterns = [
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('rooms/', RoomList.as_view(), name='room_list'),
]