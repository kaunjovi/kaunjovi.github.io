# print "Hello world from Python."

import urllib

website = "http://ctabustracker.com/bustime/map/getBusesForRoute.jsp?route=22"
url = urllib.urlopen(website)
data = url.read()

file = open("route.xml", "wb")
file.write(data)
file.close()

url.close()
