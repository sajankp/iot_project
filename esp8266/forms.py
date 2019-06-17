from django import forms
import datetime
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _


class DateForm(forms.Form):
    date = forms.DateField(label='Date',
                           initial=datetime.date.today,
                           localize=True,
                           widget=forms.TextInput(attrs={'class': 'date-input'}),
                           )
    def clean_date(self):
        data=self.cleaned_data['date']
        if data > datetime.date.today():
            raise ValidationError(_('Invalid date - future date'))
        if data < datetime.date(2019,5,2):
            raise ValidationError(_('Invalid date - try any date after 2nd May 2019'))
        return data

class DataFilterForm(forms.Form):
    week='wk'
    month='mh'
    year='yr'
    TYPE_OF_READING=[
        ('1',"Temperature"),
        ('2',"Humidity"),
    ]
    TYPE_OF_FILTER=[
        (week,"Week"),
        (month,"Month"),
        (year,"Year"),
    ]
    reading = forms.ChoiceField(label="Temperature or Humidity",
                                choices=TYPE_OF_READING,
                                initial='1'
                                )
    filter = forms.ChoiceField(label="Time Filter",
                              choices=TYPE_OF_FILTER,
                              initial='wk'
                             )
