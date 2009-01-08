from views import userRequired, render_with_user
from django.http import HttpResponseRedirect

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
    items = [
        {   'url_piece' : '1',
            'title' : 'stop#1',
            'desc' : 'for the win'
        }
    ]
    params = { 'items':items }
    return render_with_user('listoflinks.html', params)

@userRequired
def addStopDflt(r, point_name):
    urls = '/addstop/nb/'+point_name+'/'+getDefaultRegion()+'/'+getDefaultAgency()
    return HttpResponseRedirect(urls)