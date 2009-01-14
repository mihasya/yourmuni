from django import forms
from models import Bmark
from google.appengine.ext import db
from django.utils.translation import ugettext_lazy as _
from google.appengine.api import users
import re

class AddBmarkForm(forms.Form):
    name = forms.CharField(max_length=50, required=False)
    description = forms.CharField(max_length=255, required=True)

    def clean_name(self):
        #verify that the short_name is unique
        try:
            desc = self.cleaned_data['description']
        except:
            return None
        name = re.sub('[^\w|^\-| ]', '', desc)
        name = name.replace(' ', '_')
        q = db.Query(Bmark)
        q.filter('name =', name)
        q.filter('user =', users.get_current_user())
        if (q.get()):
            raise forms.ValidationError(_("A bookmark with that \
                        name exists already"))
        else:
            return name