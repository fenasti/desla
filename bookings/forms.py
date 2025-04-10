from .models import ReservationRequest
from django import forms
from django.forms import DateInput, TimeInput


class ReservationForm(forms.ModelForm):
    reservation_date = forms.DateField(widget=DateInput(attrs={'type': 'date'}))
    reservation_time = forms.TimeField(widget=TimeInput(attrs={'type': 'time'}))
    email = forms.EmailField(required=True)

    class Meta:
        model = ReservationRequest
        fields = ['details', 'reservation_date', 'reservation_time', 'email']