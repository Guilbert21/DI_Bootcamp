from django.urls import path
from .views import upload_image, filter_images

urlpatterns = [
    path('upload/', upload_image, name='upload_image'),
    path('images/', filter_images, name= 'images')
]
