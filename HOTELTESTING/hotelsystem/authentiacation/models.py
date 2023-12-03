from django.db import models

class Customer(models.Model):
    username=models.CharField(max_length=100)
    password=models.CharField(max_length=100)
    email=models.EmailField(max_length=50)
    profile_pic=models.ImageField(upload_to="media", height_field=None,  width_field=None, max_length=None,blank=True)
    phone_no= models.CharField(max_length=25)
    address=models.TextField()
    state= models.CharField(max_length=30, blank=True)
    pin_code= models.IntegerField

    def __str__(self):
        return "Customer: "+self.username
    
    class RoomManager(models.Model):
        username= models.CharField(max_length=100)
        password= models.CharField(max_length=100)
        email= models.EmailField(max_length=50)
        profile_pic=models.ImageField(upload_to="media", height_field=None,  width_field=None, max_length=None,blank=True)
        phone_no= models.CharField(max_length=25)
        gender= models.CharField(max_length=10)

        def __str__(self):
            return "Room Manager: "+self.username
        

        # https://medium.com/@great4christ2009/building-hotel-management-system-in-django-6ce524200ac4