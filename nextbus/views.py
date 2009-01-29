from shared import userRequired, render_with_user
from django.http import HttpResponseRedirect
from django.template import loader, Context
import nextbus
import google.appengine.ext.db as db
from models import Bmark, Stop
import logging


@userRequired 
def addStop(r, bmark, re=None, agency=None, route=None, 
                                                    direction=None, stop=None):
    error = ''
    if (stop is not None):
        url = nextbus.timeURL % (agency, route, direction, stop)
        q = db.Query(Bmark)
        q.filter('name = ', bmark)
        b = q.get()
        q = db.Query(Stop)
        q.filter('bmark = ', b)
        q.filter('url = ', url)
        stopObj = q.get()
        logging.info(stopObj)
        if (stopObj):
            logging.info("Stop Already Exists")
            error = "This stop has already been added"
            #it'll fall through to picking a stop again
        else:
            stopObj = Stop()
            stopObj.bmark = b
            stopObj.url = url
            stopObj.system = "nextbus"
            stopObj.put()
            #TODO: redirect to an edit page that doesnt involve the scrape
            return HttpResponseRedirect('/catch/%s' % (bmark))
    if (direction is not None):
        data = nextbus.getStops(agency, route, direction)
        prefix = '/nb/addstop/%s/%s/%s/%s/%s'\
            % (bmark, re, agency, route, direction)
        instructions = 'pick a stop'
    elif (route is not None):
        data = nextbus.getDirections(agency, route)
        prefix = '/nb/addstop/%s/%s/%s/%s' % (bmark, re, agency, route)
        instructions = 'pick a direction'
    elif (agency is not None):
        data = nextbus.getRoutes(agency)
        prefix = '/nb/addstop/%s/%s/%s' % (bmark, re, agency)
        instructions = 'pick a route'
    items = []
    if not (data):
        #todo: throw 500
        return False
    for key, value in data:
        items.append({'url_piece': key, 'title': value})
    t = loader.get_template('listoflinks.html')
    c = Context({ 'items':items, 'prefix': prefix })
    items_t = t.render(c)
    params = { 'prefix': prefix,
               'instructions': instructions,
               'list': items_t,
               'error': error }
    return render_with_user('user/addstop.html', params)

@userRequired
def addStopDflt(r, bmark):
    return addStop(r, bmark, nextbus.getDefaultRegion(),\
                                                    nextbus.getDefaultAgency())

def catchStop(r, re=None, agency=None, route=None, direction=None, stop=None):
    error = ''
    if (stop is not None):
        url = nextbus.timeURL % (agency, route, direction, stop)
        times = nextbus.getTimeURL(url)
        params = {
            'times': times
        }
        return render_with_user('single.html', params)
    if (direction is not None):
        data = nextbus.getStops(agency, route, direction)
        prefix = '/nb/catchstop/%s/%s/%s/%s'\
            % (re, agency, route, direction)
        instructions = 'pick a stop'
    elif (route is not None):
        data = nextbus.getDirections(agency, route)
        prefix = '/nb/catchstop/%s/%s/%s' % (re, agency, route)
        instructions = 'pick a direction'
    elif (agency is not None):
        data = nextbus.getRoutes(agency)
        prefix = '/nb/catchstop/%s/%s' % (re, agency)
        instructions = 'pick a route'
    items = []
    if not (data):
        #todo: throw 500
        return False
    for key, value in data:
        items.append({'url_piece': key, 'title': value})
        
    t = loader.get_template('listoflinks.html')
    c = Context({ 'items':items, 'prefix': prefix })
    items_t = t.render(c)
    params = { 'instructions': instructions,
               'list':items_t,
               'error': error }
    return render_with_user('user/addstop.html', params)
    
def catchStopDflt(r):
    return catchStop(r, nextbus.getDefaultRegion(), nextbus.getDefaultAgency())