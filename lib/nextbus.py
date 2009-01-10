from google.appengine.api import urlfetch
from BeautifulSoup import BeautifulSoup
import re

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


def scrapeList(url):
    """the lists are all identical (in theory...)"""
    result = urlfetch.fetch(url)
    if (result.status_code == 200):
        soup = BeautifulSoup(result.content)
        links = soup.html.body.findAll('a')
        pairs = {}
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
            pairs[key] = innerHTML
        return pairs
    else:
        return false
        
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
    result = urlfetch.fetch(url)
    if (result.status_code == 200):
        soup = BeautifulSoup(result.content)
        spans = soup.body.center.font.findAll('table', recursive=False)[1] \
            .findAll('span', text=re.compile('&nbsp;(\d)'))
        times = []
        for span in spans:
            times.append(span.lstrip('&nbsp;'))
        return (times)