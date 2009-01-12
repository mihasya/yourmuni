from django import forms
from models import Point
from google.appengine.ext import db
from django.utils.translation import ugettext_lazy as _
from google.appengine.api import users

class AddPointForm(forms.Form):
    name = forms.CharField(max_length=50)
    description = forms.CharField(max_length=255)
    
    def clean_name(self):
        #verify that the short_name is unique
        value = self.cleaned_data['name']
        q = db.Query(Point)
        q.filter('name =', value)
        q.filter('user =', users.get_current_user())
        if (q.get()):
            raise forms.ValidationError(_("A point with that \
                        id exists already"))
        else:
            return value