#! /usr/bin/env python
#location	city	state	zip	county	countyname	latitude	longitude
#40.20564582,-74.64750656	Hamilton	 NJ	08690	34021	Mercer	40.20564582	-74.64750656

cfile = open('counties.txt')
counties = {}
for line in cfile:
    counties[line.strip()] = 0.5
cfile.close()

f = open('sample1loc.tsv')
countyout = open('sample1loccounty.tsv','w')
countytot = {}
lines = f.read().strip().split('\n')
f.close()
maxcounty = 0
for i in range(1,len(lines)):
    cols = lines[i].strip().split('\t')
    if not countytot.has_key(cols[5]):
      countytot[cols[5]] = 0
    countytot[cols[5]] += 1
    if  countytot[cols[5]] > maxcounty:
      maxcounty = countytot[cols[5]]

countyout.write('county\tcount\n')
for k,v in countytot.iteritems():
  countyout.write('%s\t%.5f\n' % (k,v/float(maxcounty)))
  del counties[k]
for k,v in counties.iteritems():
  countyout.write('%s\t%.5f\n' % (k,v/float(maxcounty)))
countyout.close()
