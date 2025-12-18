from reservation.models import Reservation
from django import forms


class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ['date_start', 'date_end', 'payment_method']
        widgets = {
            'date_start': forms.DateInput(attrs={'type': 'date'}),
            'date_end': forms.DateInput(attrs={'type': 'date'}),
            'payment_method': forms.Select(attrs={'type': 'select'})
        }