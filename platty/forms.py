from django import forms

class EventForm(forms.Form):
    name = forms.CharField(label="Epic name?", max_length=100)
