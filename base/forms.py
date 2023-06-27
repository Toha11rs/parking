from django import forms
from parking.models import Transaction
from django.forms import DateTimeInput

class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = ['car', 'date_arrival', 'date_departure', 'price']
        widgets = {
            'date_arrival': DateTimeInput(attrs={'type': 'datetime-local'}),
            'date_departure': DateTimeInput(attrs={'type': 'datetime-local'}),
        }