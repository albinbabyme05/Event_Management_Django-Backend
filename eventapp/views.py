from django.shortcuts import render, redirect
from .models import Event
from .forms import BookingForm

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
    if request.method=='POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            print("form is valid ..saving...")
            form.save()
            print("saved.....")
            return redirect('')
        else:
            print(f"form is invalid:  {form.error}")
    
    form = BookingForm()
    dict_booking = {
        'form' : form
    }
    
    return render(request, 'booking.html', dict_booking)