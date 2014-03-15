import heatmap
import sys
"""
download heatmap package from http://jjguy.com/heatmap/
"""

f= open('sample1.coord').read().split('\n')
pts = []
for line in f:
   coords = line.strip().split('\t')
   if len(coords) < 2:
      continue
   pts.append((float(coords[1]),float(coords[0])))

hm = heatmap.Heatmap()
img = hm.heatmap(pts,dotsize=3)
hm.saveKML("heatmapjjguy.kml")
