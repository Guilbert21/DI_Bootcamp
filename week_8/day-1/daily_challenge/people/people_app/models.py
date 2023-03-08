from django.db import models

class Person(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    country = models.CharField(max_length=100)

    def __str__(self):
        return self.name