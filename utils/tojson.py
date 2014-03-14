#! /bin/bash
import sys
import json

sample = {'locations':[]}
for line in sys.stdin:
  cols = line.strip().split('\t')
  if cols[0] == "lat":
    continue
  lat = float(cols[0])
  lon = float(cols[1])
  sample['locations'].append({'lat':lat,'lon':lon})
 
print json.dumps(sample)  
    
