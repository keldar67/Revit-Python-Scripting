theLines = (
FilteredElementCollector(doc)
.OfCategory(BuiltInCategory.OST_Lines)
)

detailLines = (theLines
.Where(lambda l: 'Yes'.Equals(l.LookupParameter('Detail Line').AsValueString()))
)

modelLines = (theLines
.Where(lambda l: 'No'.Equals(l.LookupParameter('Detail Line').AsValueString()))
)

areaBoundaryLines = (
FilteredElementCollector(doc)
.OfCategory(BuiltInCategory.OST_AreaSchemeLines)
)

roomSeparationLines = (
FilteredElementCollector(doc)
.OfCategory(BuiltInCategory.OST_RoomSeparationLines)
)

print 'Detail Lines          : ' + detailLines.Count().ToString()
print 'Model Lines           : ' + modelLines.Count().ToString()
print '                        --------'
print 'Total Lines           : ' + theLines.Count().ToString()
print '\n\nAlso'
print 'Room Separation Lines : ' + roomSeparationLines.Count().ToString()
print 'Area Boundary Lines   : ' + areaBoundaryLines.Count().ToString()