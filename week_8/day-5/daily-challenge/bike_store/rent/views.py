from django.shortcuts import render
from faker import Faker
from .models import Customer

def generate_customers(request):
    fake = Faker()
    for i in range(100):
        customer = Customer()
        customer.first_name = fake.first_name()
        customer.last_name = fake.last_name()
        customer.email = fake.email()
        customer.phone_number = fake.phone_number()
        customer.address = fake.address()
        customer.city = fake.city()
        customer.country = fake.country()   
    return render(request, 'rent/generate_customers.html')

    # add vehicles
    