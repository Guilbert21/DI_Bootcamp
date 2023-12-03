from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import FormView
from django.contrib import messages
from django.urls import reverse_lazy

from .models import Room, Review
from .forms import ReviewForm, BookingForm, ContactForm

# def home(TemplateView):
#     return render(request, 'visitors/home.html')

# def about(request):
#     return render(request, 'visitors/about.html')

# def RoomList(ListView):
#     model = Room
#     context_object_name = 'room'
#     template_name = 'room_list.html'

# def RoomDetails(DetailView):

class HomeView(TemplateView):
    template_name = 'home.html'

class AboutView(TemplateView):
    template_name = 'about.html'

class RoomListView(ListView):
    model = Room
    template_name = 'room_list.html'

class RoomDetailView(DetailView):
    model = Room
    template_name = 'room_detail.html'

class BookingView(formView):
    form_class = BookingForm
    template_name = 'booking.html'
    success_url = reverse_lazy('booking_sucess')

    def form_valid(self, form):
        form.send_email()
        messages.success(self.request, 'Thank you for your booking!')


