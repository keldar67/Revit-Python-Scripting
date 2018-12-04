import collections

theMaterials = FilteredElementCollector(doc).OfCategory(BuiltInCategory.OST_Materials).ToElementIds()
#for aMaterial in theMaterials:

tranny = Transaction(doc)
try:
  tranny.Start('Deleting the Materials ')
  doc.Delete(theMaterials)
  tranny.Commit()
  tranny.Dispose()
except Exception as e:
  tranny.RollBack()
  tranny.Dispose()
  print e.message