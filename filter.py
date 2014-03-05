#! /usr/bin/env python
import sys
import random
lines = sys.stdin.read().split('\n')
s = random.sample(lines[1:],10000)
print "%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s" % ("location","city","state","zip","county","countyname","latitude","longitude")
for l in s:
    cols = l.split('\t')
    if cols[9].strip() != "" and cols[10].strip() != "" and cols[6].strip() != "" and cols[7].strip() != "" and cols[15].strip() != "" and cols[20].strip() != "":
        print "%s,%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s" % (cols[9],cols[10],cols[6].replace('u"','').replace('"',''),cols[7],cols[13],cols[15],cols[20],cols[9],cols[10])

