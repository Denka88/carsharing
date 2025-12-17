from django import forms

from reservation.models import PaymentMethod


class ReservationForm(forms.Form):
    date_start = forms.DateField()
    date_end = forms.DateField()
    payment_method = forms.ModelChoiceField(queryset=PaymentMethod.)