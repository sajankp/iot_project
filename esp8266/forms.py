from django import forms
import datetime

class DateForm(forms.Form):
    date = forms.DateField(label='Date',
                           initial=datetime.date.today,
                           localize=True,
                           widget=forms.TextInput(attrs={'class': 'date-input'}),
                           )

class DataFilterForm(forms.Form):
    week='wk'
    month='mh'
    year='yr'
    TYPE_OF_READING=[
        (1,"Temperature"),
        (2,"Humidity"),
    ]
    TYPE_OF_FILTER=[
        (week,"Week"),
        (month,"Month"),
        (year,"Year"),
    ]
    reading = forms.ChoiceField(label="Temperature or Humidity",
                                choices=TYPE_OF_READING,
                                initial=1
                                )
    filter = forms.ChoiceField(label="Time Filter",
                              choices=TYPE_OF_FILTER,
                              initial='wk'
                             )
