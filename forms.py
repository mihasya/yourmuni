from django import forms

class AddPointForm(forms.Form):
    name = forms.CharField(max_length=255)
    short_name = forms.CharField(max_length=50)
    
