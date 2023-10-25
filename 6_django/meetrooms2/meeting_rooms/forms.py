from django import forms
from .models import Room

class ReservationForm(forms.Form):
    room = forms.ModelChoiceField(queryset=Room.objects.filter(available=True))
    start_datetime = forms.DateTimeField()
    end_datetime = forms.DateTimeField()