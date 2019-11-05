theDoors = (FilteredElementCollector(doc)
.OfClass(FamilySymbol)
.OfCategory(BuiltInCategory.OST_Doors)
)

for aDoor in theDoors:
  print '\n' + aDoor.FamilyName
  params = aDoor.GetOrderedParameters()
  
  print '\tShared Params'
  for p in params: 
    if p.IsShared:
      print '\t'+ p.Definition.Name, " - ", p.GUID
  