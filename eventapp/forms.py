from django import forms
from . models import Booking

#creating a duplicate model for user to enter details
class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = '__all__'
