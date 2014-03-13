from geohash import encode
f=open('../sample2.tsv')
lines = f.read().strip().split('\n')
areas = {}
for line in lines[1:]:
  cols = line.strip().split('\t')
  lat = float(cols[0])
  lon = float(cols[1])
  geo = encode(lat,lon)[0:3]
  if not areas.has_key(geo):
     areas[geo] = 0
  areas[geo] += 1

out=open('latlon.csv','w')
out.write('lat,lon,time,value\n')
for line in lines[1:]:
  cols = line.strip().split('\t')
  lat = cols[0]
  lon = cols[1]
  geo = encode(float(lat),float(lon))[0:3]
  value = areas[geo]
  out.write('%s,%s,%s,%d\n' % (lat,lon,cols[2],value))

