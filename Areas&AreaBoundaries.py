
sortedAreas = {}

theAreas = FilteredElementCollector(doc).OfCategory(BuiltInCategory.OST_Areas)

for anArea in theAreas:
  id = anArea.AreaScheme.Id
  if not id in sortedAreas:
    sortedAreas.Add(id, [anArea])
  else:
    sortedAreas[id].Add(anArea)
    
for aScheme in sortedAreas:
  schemeName = Element.Name.GetValue(doc.GetElement(aScheme))
  print schemeName + ' - ' + sortedAreas[aScheme].Count.ToString()