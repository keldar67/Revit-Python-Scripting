import collections

theMaterials = FilteredElementCollector(doc).OfCategory(BuiltInCategory.OST_Materials).ToElementIds()
theAppearanceAssets = FilteredElementCollector(doc).OfClass(AppearanceAssetElement).ToElementIds()

tranny = Transaction(doc)
try:
  tranny.Start('Deleting the Materials & Assets')
  print 'Deleteing Materials'
  doc.Delete(theMaterials)
  print 'Deleting AppearanceAssets'
  doc.Delete(theAppearanceAssets)
  
  tranny.Commit()
  tranny.Dispose()
except Exception as e:
  tranny.RollBack()
  tranny.Dispose()
  print e.message