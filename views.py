from google.appengine.api import users
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from models import *
from forms import *
import google.appengine.ext.db
from lib import nextbus

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
        q = db.Query(Bmark)
        q.filter('user = ', user)
        bmarks = q.fetch(limit=200)
        links = [ { 'url':'/addbmark', 'title':'add a bookmark' } ]
        param = { 'bmarks': bmarks, 'links': links }
        return render_with_user('user/home.html', param)
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
def addBmark(r):
    if (r.method) == 'POST':
        form = AddBmarkForm(r.POST)
        if (form.is_valid()):
            bm = Bmark()
            bm.user = users.get_current_user()
            bm.name = form.cleaned_data['name']
            bm.desc = form.cleaned_data['description']
            bm.put()
            url = '/addstop/'+getDefaultSource()+'/'+bm.name+'/_dflt'
            return HttpResponseRedirect(url)
    else:
        form = AddBmarkForm()
    return render_with_user('user/addbmark.html', {'form':form})
        
@userRequired
def catch(r, bmark):
    q = db.Query(Bmark)
    q.filter('name =', bmark)
    bm = q.get()
    q = db.Query(Stop)
    q.filter('bmark = ', bm)
    stops = []
    error = None
    for row in q:
        stopInfo = nextbus.getTimeURL(row.url)
        if (stopInfo):
            stops.append(stopInfo)
        else:
            error = "Some stops could not be retreived"

    links = [ { 'url':'/addstop/nb/%s/_dflt' % (bmark), 'title':'add a stop' },
              { 'url':'/catch/%s' % bmark, 'title':'reload'}]

    params = {
        'bmark_name': bm.name,
        'bmark_desc': bm.desc,
        'stops': stops,
        'links': links,
        'error': error
    }
    return render_with_user('user/catch.html', params)

@userRequired
def clearCache(r):
    import logging
    from google.appengine.api import memcache
    if users.is_current_user_admin():
        logging.info("Flushing Cache")
        memcache.flush_all()
    return home(r)