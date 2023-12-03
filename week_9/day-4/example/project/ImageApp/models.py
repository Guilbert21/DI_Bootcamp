from django.db import models
from django.contrib.auth.models import User

class Image(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/')
    description = models.CharField(max_length=100)
    upload_date = models.DateTimeField(auto_now_add=True)
    

