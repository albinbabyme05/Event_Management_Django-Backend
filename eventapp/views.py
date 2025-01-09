from django.shortcuts import render
from .models import Event

# Create your views here.

def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def events(request):
    dict_event = {
        # to diplay the field in the model.py should render in event.html
        'event': Event.objects.all() 
    }
    return render(request, 'events.html', dict_event)

def contact(request):
    return render(request, 'contact.html')

def booking(request):
    return render(request, 'booking.html')