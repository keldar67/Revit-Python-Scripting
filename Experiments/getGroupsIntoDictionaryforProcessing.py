theModelGroups = (
  FilteredElementCollector(doc)
  .OfCategory(BuiltInCategory.OST_IOSModelGroups)
  .WhereElementIsNotElementType()
  )
  
# sort the groups into a dictionary of
# start with an empty dictionary
theGroups = {}

# Loop through the Element Collector and 
# test each group and sort it accordingly
i = 0

for aModelGroup in theModelGroups:
  i = i + 1
  print i
  # If the groups type is already in the dictionary
  theId = aModelGroup.GroupType.Id.ToString()
  if theId in theGroups.keys():
    # Add this Model Group to that list
    theGroups[theId].Append(aModelGroup)
    print theId
  else:
    # Create a new dictionary with an associated list
    # with this group as its first list member 
    theGroups.Add(theId,[aModelGroup])

for aGroup in theGroups.Keys:

  print len(theGroups[aGroup])
  
  
    
    