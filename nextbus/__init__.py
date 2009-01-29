from google.appengine.api import urlfetch
from BeautifulSoup import BeautifulSoup
from google.appengine.api import memcache
import re
import cPickle as pickle
import logging
from sys import setrecursionlimit
setrecursionlimit(4000)

agencyURL = "http://www.nextbus.com/wireless/miniAgency.shtml?re=%s"
routeURL = "http://www.nextbus.com/wireless/miniRoute.shtml?a=%s"
directionURL = "http://www.nextbus.com/wireless/miniDirection.shtml?a=%s&r=%s"
stopsURL="http://www.nextbus.com/wireless/miniStop.shtml?a=%s&r=%s&d=%s"
timeURL="http://www.nextbus.com/wireless/miniPrediction.shtml?a=%s&r=%s&d=%s&s=%s"

#hardcoded for now, since its very difficul to scrape the nextbus region listing
#in its raw form without an iphone ua, and appengine won't let me fake ua
regions = [
'Alberta',
'Arizona',
'California-Northern',
'California-Southern',
'Colorado',
'Delaware',
'Florida',
'Georgia',
'Illinois',
'Maryland',
'Massachusetts',
'New Jersey',
'New York',
'North Carolina',
'Ohio',
'Oklahoma',
'Ontario',
'Oregon',
'Pennsylvania',
'South Carolina',
'Virginia',
'Washington',
'Wyoming'
]

defaultRegion='California-Northern'
defaultAgency='sf-muni'

def getDefaultRegion():
    """return the default region for user (norcal for now)"""
    return defaultRegion

def getDefaultAgency():
    """return the default agency for the user (sf-muni for now)"""
    return defaultAgency


def scrapeList(url):
    """the lists are all identical (in theory...)"""
    result = urlfetch.fetch(url)
    if (result.status_code == 200):
        soup = BeautifulSoup(result.content)
        links = soup.html.body.findAll('a')
        pairs = []
        for x in links:
            #verify that the link is something we want, in case nextbus adds
            #stupid links to their pages
            if (x['href'].find('mini') == -1):
                pass
            #the interesting bit is always the last arg
            lastEq = x['href'].rfind('=')+1
            key = x['href'][lastEq:]
            """nextbus devs are terrible at writing markup and use a different
            combination of <a>, <font>, and <nobr> tags on every page that
            displays a list that looks the exact fucking same. To combat this
            epic display of fail, I iterate over the contents of each <a> tag 
            until I find the innermost child"""
            child = x.contents[0]
            lastChild = child
            try:
                while (child.contents):
                    lastChild = child
                    child = child.contents[0]
            except AttributeError:
                innerHTML = lastChild.string
            pairs.append([key,innerHTML])
        return pairs
    else:
        return False
        
def scrapeRegions():
    return regions

def scrapeAgencies(region):
    url = agencyURL % (region)
    return scrapeList(url)
    
def scrapeRoutes(agency):
    url = routeURL % (agency)
    return scrapeList(url)

def scrapeDirections(agency, route):
    url = directionURL % (agency, route)
    return scrapeList(url)
    
def scrapeStops(agency, route, direction):
    url = stopsURL % (agency, route, direction)
    return scrapeList(url)
    
def scrapeTime(agency, route, direction, stop):
    """the prediction page is not a list, so it gets its own scrape code"""
    url = timeURL % (agency, route, direction, stop)
    return scrapeTimeURL(url)

def scrapeTimeURL(url):
    """the prediction page is not a list, so it gets its own scrape code"""
    try:
        result = urlfetch.fetch(url)
    except:
        return False
    if (result.status_code == 200):
        soup = BeautifulSoup(result.content)
        infoTable = soup.body.center.font.findAll('table', recursive=False)[0]
        route = infoTable.findAll('font', text=re.compile('Route'))[0] \
                .findNext('b').string
        stop = infoTable.findAll('font', text=re.compile('Stop'))[0] \
            .findNext('b').string
        try:
            spans = soup.body.center.font.findAll('table', recursive=False)[1] \
            .find('tr').findAll('span', text=re.compile('&nbsp;(\d+|[A-Z]\w+)'))
            times = []
            for span in spans:
                times.append(span.lstrip('&nbsp;'))
        except:
            times = None
        response = {
            'route': route,
            'stop': stop,
            'times': times
        }
        return (response)
    else:
        return False
        
def getRegions():
    """Get a listing of the regions
    For now, just return the scrape. When I actually start using this, will
    need to add caching"""
    return scrapeRegions()
    
def getAgencies(region):
    key = "agencies_%s" % region
    agencies = memcache.get(key)
    if (agencies):
        logging.info("Got agencies from memcache")
        return pickle.loads(agencies)
    else:
        agencies = scrapeAgencies(region)
        if not (agencies):
            return False
        else:
            try:
                logging.info("Saving agencies to memcache")
                value = pickle.dumps(agencies)
                memcache.set(key, value, 60*60*24)
            except:
                logging.error("FAIL: Saving agencies to memcache")
            return agencies
    
def getRoutes(agency):
    key = "routes_%s" % (agency)
    routes = memcache.get(key)
    if (routes):
        logging.info("Got routes from memcache")
        return pickle.loads(routes)
    else:
        routes = scrapeRoutes(agency)
        if not (routes):
            return False
        else:
            try:
                logging.info("Saving routes to memcache")
                value = pickle.dumps(routes)
                memcache.set(key, value, 60*60*24)
            except:
                logging.error("FAIL: Saving routes to memcache")
            return routes
    
def getDirections(agency, route):
    key = "directions_%s_%s" % (agency, route)
    directions = memcache.get(key)
    if (directions):
        logging.info("Got directions from memcache")
        return pickle.loads(directions)
    else:
        directions = scrapeDirections(agency, route)
        if not (directions):
            return False
        else:
            try:
                logging.info("Saving directions to memcache")
                value = pickle.dumps(directions)
                memcache.set(key, value, 60*60*24)
            except:
                logging.error("FAIL: Saving directions to memcache")
            return directions
    
def getStops(agency, route, direction):
    key = "stops_%s_%s_%s" % (agency, route, direction)
    stops = memcache.get(key)
    if (stops):
        logging.info("Got stops from memcache")
        return pickle.loads(stops)
    else:
        stops = scrapeStops(agency, route, direction)
        if not (stops):
            return False
        else:
            try:
                logging.info("Saving stops to memcache")
                value = pickle.dumps(stops)
                memcache.set(key, value, 60*60*24)
            except:
                logging.error("FAIL: Saving stops to memcache")
            return stops
    
def getTime(agency, route, direction, stop):
    """this won't need caching since we want the latest info"""
    return scrapeTime(agency, route, direction, stop)

def getTimeURL(url):
    key = "time_%s" % url
    times = memcache.get(key)
    if (times):
        logging.info("Got time from memcache")
        return pickle.loads(times)
    else:
        times = scrapeTimeURL(url)
        if not (times):
            return False
        else:
            try:
                logging.info("Saving time to memcache")
                value = pickle.dumps(times)
                memcache.set(key, value, 15)
            except:
                logging.error("FAIL:Saving time to memcache")
            return times
