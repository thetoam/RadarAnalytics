import numpy as np

def main():
  fileName = "data/hotspot_historic.csv"

  lats = (-44.0, -10.0)
  lons = (113.0, 154.0)
  resolution = 1.0

  latSize = (lats[1] - lats[0]) / resolution
  lonSize = (lons[1] - lons[0]) / resolution

  print lonSize
  print latSize

  aCounts = np.zeros((latSize, lonSize))

  k = 0
  j = 0
  i = 0
  try:
    with open(fileName, "r") as f:
      for line in f:
        d = line.split(",")
        if d[0] == "FID":
          continue
        lat = float(d[14])
        lon = float(d[15])

        if lat > lats[0] and lat < lats[0] and lon > lons[0] and lon < lons[1]:
          iLat = int((lat - lats[0]) / resolution)
          iLon = int((lon - lons[0]) / resolution)
          aCounts[iLat, iLon] += 1

        
        
  except:
    raise









main()
