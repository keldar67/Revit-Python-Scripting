#========================================================================#
#      _____               __                            
#      \_   \__ _ _ __     \ \  __ _ _ __ ___   ___  ___ 
#       / /\/ _` | '_ \     \ \/ _` | '_ ` _ \ / _ \/ __|
#    /\/ /_| (_| | | | | /\_/ / (_| | | | | | |  __/\__ \
#    \____/ \__,_|_| |_| \___/ \__,_|_| |_| |_|\___||___/
#
#
#  November 2019
#
#  Automation of Project Setup 
#
#  This script automates specifying coordinates in relation to the 
#  City of Sydney (CoS) Model or City of Brisbane (CoB) model.
#
#  CITY of SYDNEY
#  Easting  =   335,000 meters
#  Northing = 6,250,000 meters
#
#  CITY of BRISBANE
#  Easting  =   500,000 meters
#  Northing = 6,960,000 meters
#
#  Elevations is set to 0.0 meters
#
#  Angle to True North is also set to 0°0'0"
#
#Instructions:
#If within City models for BNE or SYD
# Enter 'BNE' or 'SYD' between the quote below 
# If not then leave blank and enter custom values insteard
city = 'SYD'
#
# Enter Custom Values here by replaceing 0.0 with your value
_N = 0.0
_E = 0.0
#
#========================================================================#
city = 'SYD'
#city = 'BNE'
#------------------------------------------------------------------------#

if 'SYD'.Equals(city):
  Northing = 6250000000
  Easting = 335000000
else:
  if 'BNE'.Equals(city):
    Northing = 6960000000
    Easting = 500000000
  else:
    Northing = _N
    Easting = _E
  
Elevation = 0.0
Angle = 0.0
FEET = 304.8

#Get the Project Basepoint
pbp = FilteredElementCollector(doc).OfCategory(BuiltInCategory.OST_ProjectBasePoint).FirstElement()

tranny = Transaction(doc)
try:
  tranny.Start('Setting Project Basepoint Value to CoS')
  
  N = pbp.LookupParameter('N/S')
  E = pbp.LookupParameter('E/W')
  H = pbp.LookupParameter('Elev')
  A = pbp.LookupParameter('Angle to True North')
  
  N.Set(Northing/FEET)
  print 'settng N'
  E.Set(Easting/FEET)
  print 'settng E'
  H.Set(Elevation/FEET)
  print 'settng H'
  A.Set(Angle)
  print 'settng A'
  
  
  tranny.Commit()
  tranny.Dispose()
except Exception as e:
  if tranny.HasStarted:
    tranny.RollBack()
    tranny.Dispose()
    print '+---- Error -----+'
    print e.message