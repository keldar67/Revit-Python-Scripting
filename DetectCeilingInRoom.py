theRooms = (
FilteredElementCollector(doc)
.OfCategory(BuiltInCategory.OST_Rooms)
)

theCeilings = (
FilteredElementCollector(doc)
.OfCategory(BuiltInCategory.OST_Ceilings)
.WhereElementIsNotElementType()
)

print "Rooms = " + theRooms.Count().ToString()
print "Ceilings = " + theCeilings.Count().ToString()

for aRoom in theRooms:
  pass
  #Outline.ContainsOtherOutline(CeilingOutline,0.25)