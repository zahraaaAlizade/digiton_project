from django import forms
from .models import User, Reservation, Room


class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ['customer', 'room', 'Phone', 'Email', 'FromDate', 'toDate']
