from google.appengine.api import users
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from models import *
from forms import *
import google.appengine.ext.db

defaultSource='nb'

def getDefaultSource():
    """return the default source site for user (nextbus for now)"""
    return defaultSource

def render_with_user(tpl, vars={}):
    vars['user'] = users.get_current_user()
    return render_to_response(tpl, vars)
    
def home(r):    
    user = users.get_current_user()
    if (user):
        q = db.Query(Point)
        q.filter('user = ', user)
        points_list = q.fetch(limit=200)
        return render_with_user('user/home.html', {'points':points_list})
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
            pt = Point()
            pt.user = users.get_current_user()
            pt.name = form.cleaned_data['short_name']
            pt.desc = form.cleaned_data['name']
            pt.put()
            url = '/addstop/'+getDefaultSource()+'/'+pt.name+'/_dflt'
            return HttpResponseRedirect(url)
    else:
        form = AddPointForm()
    return render_with_user('user/addpoint.html', {'form':form})
        
@userRequired
def catch(r, point_name):
    params = {
        'point_name': point_name,
    }
    return render_with_user('user/catch.html', params)