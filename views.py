from google.appengine.api import users
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
    
def render_with_user(tpl, vars={}):
    vars['user'] = users.get_current_user()
    return render_to_response(tpl, vars)
    
def home(r):    
    user = users.get_current_user()
    if (user):
        return render_with_user('user/home.html')
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
    return render_with_user('user/addpoint.html')
    
@userRequired 
def addStop(r, point_name, route=None, direction=None, stop=None):
    params = {}
    return render_with_user('user/addstop.html', params)
    
        