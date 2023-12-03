from django.db import models
from django.contrib.auth.models import User
# from django.urls import reverse
from .models import Models

class Country():
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class Category():
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class Director():
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    
# create a class form film
class Film(models.Model):
    title = models.CharField(max_length=100)
    release_date = models.DateField(auto_now_add=True)
    created_in_country = models.ForeignKey(Country, on_delete=models.CASCADE, related_name="films_country")
    available_in_countries = models.ManyToManyField(Country, related_name="films_available")
    category = models.ManyToManyField(Category, related_name="films_category")
    director = models.ManyToManyField("Director", related_name="films_category")

    def __str__(self):
        return self.title
    

class Comment(models.Model):
    film = models.ForeignKey(Film, on_delete=models.CASCADE, related_name="comments")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comments")
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)



# from django.db import models
# from django.contrib.auth.models import User
# # from django.urls import reverse
# from .models import Models

# class Country():
#     name = models.CharField(max_length=100)

#     def __str__(self):
#         return self.name
    
# class Category():
#     name = models.CharField(max_length=100)

#     def __str__(self):
#         return self.name
    
# class Director():
#     first_name = models.CharField(max_length=100)
#     last_name = models.CharField(max_length=100)

#     def __str__(self):
#         return f"{self.first_name} {self.last_name}"

    
# # create a class form film
# class Film(models.Model):
#     title = models.CharField(max_length=100)
#     release_date = models.DateField(auto_now_add=True)
#     created_in_country = models.ForeignKey(Country, on_delete=models.CASCADE, related_name="films_country")
#     available_in_countries = models.ManyToManyField(Country, related_name="films_available")
#     category = models.ManyToManyField(Category, related_name="films_category")
#     director = models.ManyToManyField("Director", related_name="films_category")

#     def __str__(self):
#         return self.title
    

# class Comment(models.Model):
#     film = models.ForeignKey(Film, on_delete=models.CASCADE, related_name="comments")
#     user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comments")
#     text = models.TextField()
#     created_at = models.DateTimeField(auto_now_add=True)
