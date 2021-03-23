
# Get all of th levels in the Project
theLevels = FilteredElementCollector(doc).OfCategory(BuiltInCategory.OST_Levels).WhereElementIsNotElementType()

# Get all of th Rooms in the Project
theRooms = FilteredElementCollector(doc).OfCategory(BuiltInCategory.OST_Rooms)

# Get all of th Ceilings in the Project
theCeilings = FilteredElementCollector(doc).OfCategory(BuiltInCategory.OST_Ceilings).WhereElementIsNotElementType()

roomsByLevel = {}
ceilingsByLevel = {}

def BoundaryfromRoom(aRoom):
  # Set the Room Calculation Options first
  options = SpatialElementBoundaryOptions()
  # Set the Options to Finished face of the bounding wall
  options.SpatialElementBoundaryLocation = SpatialElementBoundaryLocation.Finish
  
  # Then Get the list of Boundaries
  # These come as a list, where internal loops may exist.
  # We are primarily interested in the first being the outer boundary
  theBoundaries = aRoom.GetBoundarySegments(options)
  
  for aBoundary in theBoundaries[0]: 
    boundaryLength = (aBoundary.GetCurve().ApproximateLength * 304.8).ToString()
    print ' -- : ' + boundaryLength 

# Loop through all of the levels
for aLevel in theLevels:
  print Element.Name.GetValue(aLevel)
  # Sort all of the rooms to levels
  for aRoom in theRooms:
    if aRoom.LevelId.Equals(aLevel.Id):
      roomName = Element.Name.GetValue(aRoom)
      print ' - ' + roomName
      BoundaryfromRoom(aRoom)
      
      #If this level doesn't have a list yet create it and add the room
      if not aLevel.Name in roomsByLevel.Keys:
        # Create a new list with aRoom as the first list element.
        roomsByLevel.Add(aLevel.Name,[aRoom])
      else:
        # Find the existing list and add the room to that instead
        roomsByLevel[aLevel.Name].Add(aRoom)
  print ' ===== '    
  #Sort all of the ceilings to levels
  for aCeiling in theCeilings:
    if aCeiling.LevelId.Equals(aLevel.Id):
      CeilingTypeName = Element.Name.GetValue(doc.GetElement(aCeiling.GetTypeId()))
      print ' - ' + CeilingTypeName
      
      #If this level doesn't have a list yet create it and add the room
      if not aLevel.Name in ceilingsByLevel.Keys:
        # Create a new list with aRoom as the first list element.
        ceilingsByLevel.Add(aLevel.Name,[aCeiling])
      else:
        # Find the existing list and add the room to that instead
        ceilingsByLevel[aLevel.Name].Add(aCeiling)
        
        
        