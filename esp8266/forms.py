from django import forms
import datetime

class DateForm(forms.Form):
    date = forms.DateField(label='Date',
                           initial=datetime.date.today,
                           localize=True,
                           widget=forms.TextInput(attrs={'class': 'date-input'}),
                           )
