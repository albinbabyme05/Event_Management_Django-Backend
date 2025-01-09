from django import forms
from . models import Booking

class DateInput(forms.DateInput):
    input_type = 'date'
    
#creating a duplicate model for user to enter details
class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = '__all__'
        
        #add date picker
        widgets = {
            'bookingDate' : DateInput(),
        }

        #to change the labels
        labels = {
             'customerName': "Customer Name:",
             'customerPhone' : "Customer Phone:",
             'name' : "Event Name:",
              'bookingDate' : "Booking Date:",
        }