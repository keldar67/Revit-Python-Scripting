


def getSitePoints():
  things = (
  FilteredElementCollector(doc)
  .OfCategory(BuiltInCategory.OST_IOS_GeoSite)
  .ToList()
  )
  
  return things

def getPBP():
  points = getSitePoints()
  for p in points:
    if type(p) == BasePoint:
      return p
  return None

def getOrigin():
  points = getSitePoints()
  for p in points:
    if type(p) == InternalOrigin:
      return p
  return None
  
  
pbp = getPBP()
io = getOrigin()


    
    