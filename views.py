from google.appengine.api import users
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from models import *
from forms import *

def render_with_user(tpl, vars={}):
    vars['user'] = users.get_current_user()
    return render_to_response(tpl, vars)
    
def home(r):    
    user = users.get_current_user()
    if (user):
        #TODO: make this only get points for the current user
        #figure out datastore API
        pt = point()
        points = pt.all()
        #TODO: figure out how to display Query objects in templates
        return render_with_user('user/home.html', {'points':points})
    else:
        return render_to_response('splash.html');

def login(r):
    return HttpResponseRedirect(users.create_login_url('/'))

def logout(r):
    return HttpResponseRedirect(users.create_logout_url('/'))
    


def userRequired(fn):
    """decorator for forcing a login"""
    def new(*args, **kws):
        user = users.get_current_user()
        if not (user):
            r = args[0]
            return HttpResponseRedirect(users.create_login_url(
                                            r.build_absolute_uri()))
        else:
            return fn(*args, **kws)
    return new

@userRequired    
def addPoint(r):
    if (r.method) == 'POST':
        form = AddPointForm(r.POST)
        if (form.is_valid()):
            pt = point()
            pt.user = users.get_current_user()
            pt.name = form.cleaned_data['short_name']
            pt.desc = form.cleaned_data['name']
            pt.put()
    else:
        form = AddPointForm()
    return render_with_user('user/addpoint.html', {'form':form})
    
@userRequired 
def addStop(r, point_name, route=None, direction=None, stop=None):
    params = {}
    return render_with_user('user/addstop.html', params)
    
        