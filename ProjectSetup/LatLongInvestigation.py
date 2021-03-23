# Get and Print the Current Site Location
#
# The actual Conversion is as follows
#
# AngleInRadians * 180 / math.pi 
#
# or AngleInRadians * 57.295779513082323
#
# siteLocation.Latitude * 180 / math.pi
# -33.867137908935547﻿
#
# To convert back the other way
#
# interalUnits = AngleInDegrees * (180/math.pi)
#
import math

DoIt = False

projectLocation = doc.ActiveProjectLocation
siteLocation = projectLocation.GetSiteLocation()

lat = siteLocation.Latitude
lon = siteLocation.Longitude

print 'Internal Units'
print 'Lat : ' + lat.ToString()
print 'Lon : ' + lon.ToString()
print '\n'
print 'Converted to decimal degrees'
print UnitUtils.ConvertFromInternalUnits(siteLocation.Latitude, DisplayUnitType.DUT_DECIMAL_DEGREES)
print UnitUtils.ConvertFromInternalUnits(siteLocation.Longitude, DisplayUnitType.DUT_DECIMAL_DEGREES)
print '\n'
print 'Converted back to radians'
print 
print

newLat = -27.46857 / (180/math.pi)
newLon = 153.02969 / (180/math.pi)

print newLat
print newLon


if DoIt:
  tranny = Transaction(doc)
  try:
    tranny.Start('Setting Coordinates to Brisbane Office')
    siteLocation.Latitude = newLat
    siteLocation.Longitude = newLon
    if tranny.HasStarted():
      tranny.Commit()
      tranny.Dispose
  except Exception as e:
    print e.message
    tranny.RollBack()
    tranny.Dispose
