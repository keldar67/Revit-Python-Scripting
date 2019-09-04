theDoors = (
FilteredElementCollector(doc)
.OfClass(FamilyInstance)
.OfCategory(BuiltInCategory.OST_Doors)
.Where(lambda aDoor: 'TBC'.Equals(aDoor.LookupParameter('Mark').AsString()))
.ToList()
)

for aDoor in theDoors: 
	#print aDoor.LookupParameter('Mark').AsString()
	print 'Door: ' + aDoor.Id.ToString() + ' - Host: ' + aDoor.Host.Id.ToString()