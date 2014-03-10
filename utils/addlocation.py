#! /usr/bin/env python
from geohash import encode
import sys
import math

class ZipCode(object):
  def __init__(self):
    self.loadZips()

  def distance(self, origin, destination):
    lat1, lon1 = origin
    lat2, lon2 = destination
    radius = 6371 # km

    dlat = math.radians(lat2-lat1)
    dlon = math.radians(lon2-lon1)
    a = math.sin(dlat/2) * math.sin(dlat/2) + math.cos(math.radians(lat1)) \
        * math.cos(math.radians(lat2)) * math.sin(dlon/2) * math.sin(dlon/2)
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
    d = radius * c

    return d

  def loadZips(self):
    sf = open('states.txt')
    states = {}
    for line in sf:
      cols = line.strip().split(' ')
      states[cols[0]] = cols[1]
   
    f = open('uszip.txt')

    self.zips = {}
    for line in f:
      cols = line.strip('\n').split('\t')
      zipc = cols[1]
      city = cols[2]
      statename = cols[3]
      state = cols[4]
      countyname = cols[5]
      county = cols[6]
      lat = float(cols[9])
      lon = float(cols[10])
      ghash = encode(lat,lon)[0:4]
      if not states.has_key(state):
          continue
      if not self.zips.has_key(ghash):
         self.zips[ghash] = []
      self.zips[ghash].append({'zipc':zipc,
                               'city': city, 
                               'state': state, 
                               'statename': statename, 
                               'county': states[state] + county, 
                               'countyname': countyname, 
                               'lat':lat,'lon':lon})
   
  def get(self,lat,lon):
    mhash = encode(lat,lon)[0:4]
    minzip = None
    if self.zips.has_key(mhash):
      mindist = -1
      for candidate in self.zips[mhash]:
        dist = self.distance([lat,lon],[candidate['lat'],candidate['lon']])
        if mindist == -1 or dist < mindist:
            mindist = dist
            minzip = candidate 
    return minzip
  
if __name__ == '__main__':     
  import sys
  latcol = long(sys.argv[1])
  loncol = long(sys.argv[2])
  header = True
  zipcode = ZipCode() 
  for line in sys.stdin:
    cols = line.strip().split('\t')
    if header:
      cols.extend(["state","statename","county","countyname","city","zip"])
      print "\t".join(cols) 
      header = False
      continue
    lat = float(cols[latcol])
    lon = float(cols[loncol])
    geo = zipcode.get(lat,lon) 
    if geo is None:
      continue
    cols.extend([geo['state'],geo['statename'],geo['county'],geo['countyname'],geo['city'],geo['zipc']])
    print "\t".join(cols)
