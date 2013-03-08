import feedparser
import urllib2
import xml.etree.ElementTree as ET

rss_query = 'feed://weather.yahooapis.com/forecastrss?w=%s&u=c'
woeid_query = "http://where.yahooapis.com/v1/places.q('%s')?appid=lPNQkerV34G6qQpJY6La2AD9gmAbbe4QfzM6cuiZ55L4YOGPlSS.S8w80QHZBgvx1y.zZsnNSriQbMq6c19vfeYSzs7rxSI-"
placetag = '{http://where.yahooapis.com/v1/schema.rng}place'
woeidtag = '{http://where.yahooapis.com/v1/schema.rng}woeid'

def get_woeid(city, province, country):
    location = '%20'.join((city, province, country))
    url = woeid_query % (location)
    request = urllib2.Request(url)
    u = urllib2.urlopen(request)
    tree = ET.parse(u)
    rootElem = tree.getroot()
    return rootElem.find(placetag).find(woeidtag).text

def weather_now(city, province, country):
    woeid = get_woeid(city, province, country)
    url = rss_query % str(woeid)
    feed = feedparser.parse(url)
    status = feed['entries'][0]['yweather_condition']
    del status['code']
    return status


def weather_forcast(city, province, country):
    woeid = get_woeid(city, province, country)
    url = rss_query % str(woeid)
    feed = feedparser.parse(url)
    status = feed['entries'][0]['yweather_forecast']
    del status['code']
    return status

# print weather_forcast('shanghai', 'shanghai', 'china')
# print weather_now('shanghai', 'shanghai', 'china')
