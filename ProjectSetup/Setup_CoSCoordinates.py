#========================================================================#
#      _____               __                            
#      \_   \__ _ _ __     \ \  __ _ _ __ ___   ___  ___ 
#       / /\/ _` | '_ \     \ \/ _` | '_ ` _ \ / _ \/ __|
#    /\/ /_| (_| | | | | /\_/ / (_| | | | | | |  __/\__ \
#    \____/ \__,_|_| |_| \___/ \__,_|_| |_| |_|\___||___/
#
#  Automation of Project Setup 
#
#  This script automates specifying coordinates in relation to the 
#  City of Sydney (CoS) Model.
#
#  Easting  =   335,000 meters
#  Northing = 6,250,000 meters
#
#  Elevations is set to 0.0 meters
#
#  Angle to True North is also set to 0°0'0"
#
#
#  November 2019
#
#========================================================================#

#------------------------------------------------------------------------#

Northing = 6250000000
Easting = 335000000
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
  A.Set(Angle/FEET)
  print 'settng A'
  
  
  tranny.Commit()
  tranny.Dispose()
except Exception as e:
  if tranny.HasStarted:
    tranny.RollBack()
    tranny.Dispose()
    print '+---- Error -----+'
    print e.message