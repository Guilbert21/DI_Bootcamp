from django.contrib import admin
from .models import Customer, VehicleType, VehicleSize, Vehicle, RentalRate, Rental


admin.site.register(Vehicle)
admin.site.register(VehicleSize)
admin.site.register(VehicleType)
admin.site.register(Customer)
admin.site.register(RentalRate)
admin.site.register(Rental)
