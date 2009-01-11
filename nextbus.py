from views import userRequired, render_with_user
from django.http import HttpResponseRedirect
from lib import nextbus

defaultRegion='California-Northern'
defaultAgency='sf-muni'


def getDefaultRegion():
    """return the default region for user (norcal for now)"""
    return defaultRegion

def getDefaultAgency():
    """return the default agency for the user (sf-muni for now)"""
    return defaultAgency



@userRequired 
def addStop(r, point_name, re=None, agency=None, route=None, 
                                                    direction=None, stop=None):
    if (stop is not None):
        #todo: add stop to point
        pass
    elif (direction is not None):
        data = nextbus.getStops(agency, route, direction)
        prefix = '/addstop/nb/%s/%s/%s/%s/%s'\
            % (point_name, re, agency, route, direction)
    elif (route is not None):
        data = nextbus.getDirections(agency, route)
        prefix = '/addstop/nb/%s/%s/%s/%s' % (point_name, re, agency, route)
    elif (agency is not None):
        data = nextbus.getRoutes(agency)
        prefix = '/addstop/nb/%s/%s/%s' % (point_name, re, agency)

    items = []
    if not (data):
        #todo: throw 500
        return False
    for key in data:
        items.append({'url_piece': key, 'title': data[key]})
    params = { 'items':items,
           'prefix': prefix }
    return render_with_user('listoflinks.html', params)

@userRequired
def addStopDflt(r, point_name):
    url='/addstop/nb/'+point_name+'/'+getDefaultRegion()+'/'+getDefaultAgency()
    return HttpResponseRedirect(url)