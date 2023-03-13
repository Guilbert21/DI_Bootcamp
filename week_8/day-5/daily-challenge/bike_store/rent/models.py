from django.db import models
from django.utils import timezone

class Customer(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone_number = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
    
class VehicleType(models.Model):
    name = models.CharField(max_length=100)
    
class VehicleSize(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class Vehicle(models.Model):
    vehicle_type = models.ForeignKey(VehicleType, on_delete=models.CASCADE)
    vehicle_size = models.ForeignKey(VehicleSize, on_delete=models.CASCADE)
    price = models.FloatField()
    date_created = models.DateField(default=timezone.now)
    
    def __str__(self):
        return f'{self.vehicle_type} {self.vehicle_size}'
    
class RentalRate(models.Model):
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    days = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    
    def __str__(self):
        return f'{self.vehicle} {self.days} days'
    
class Rental(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    date_created = models.DateField(default=timezone.now)
    
    def __str__(self):
        return f'{self.customer} {self.vehicle} {self.start_date} {self.end_date}'
    
    