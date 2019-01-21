
#--------------------------------------------------------------------------
def GetAllMaterials():
  theMaterials = (
  FilteredElementCollector(doc)
  .OfCategory(BuiltInCategory.OST_Materials)
  .OrderBy(lambda m: m.Name)
  .ToList()
  )
  return theMaterials
#--------------------------------------------------------------------------
def GetAllAppearanceAssets():
  theAppearanceAssets = (
  FilteredElementCollector(doc)
  .OfCategory(BuiltInCategory.OST_AppearanceAsset)
  .OrderBy(lambda aa: aa.Name)
  .ToList()
  )
  return theAppearanceAssets
#--------------------------------------------------------------------------
def ReportMaterial(theMaterial):
  TabIdentity(theMaterial)
  TabGraphics(theMaterial)
  TabAppearance(theMaterial)
#--------------------------------------------------------------------------
def GetRGB(theColor):
  col = 'RGB '
  col = col + theColor.Red.ToString() + '-'
  col = col + theColor.Green.ToString() + '-'
  col = col + theColor.Blue.ToString()
  return col
#--------------------------------------------------------------------------
def GetPatterns(theMaterial):
  print 'SURFACE PATTERN'
  print 'ForeGround'
  print 'Pattern: '
  print 'Color: ' 
  print 'Background'
  print 'Pattern: '
  print 'Color: '
  print '\n'
  print 'CUT PATTERN'
  print 'ForeGround'
  print 'Pattern: ' + doc.GetElement(mat.CutForegroundPatternId).Name
  print 'Color: ' + GetRGB(theMaterial.CutForegroundPatternColor)
  print 'Background'
  print 'Pattern: ' + doc.GetElement(mat.CutBackgroundPatternId).Name
  print 'Color: '+ GetRGB(theMaterial.CutBackgroundPatternColor)
  
  
#--------------------------------------------------------------------------
def TabIdentity(theMaterial):
  print '+----------------+'
  print '| TAB - Identity |'
  print '+----------------+'
  print 'Name: ' + theMaterial.Name
  print '+-----------------------------+'
  print 'Descriptive Information'
  print 'Descritpion: '
  print 'Class: ' + theMaterial.MaterialClass
  print 'Comments: '
  print 'Keywords: '
  print '+-----------------------------+'
  print 'Product Information'
  print 'Manufacturer: '
  print 'Model: '
  print 'Cost: '
  print 'URL: '
  print '+-----------------------------+'
  print 'Revit Annotation Information'
  print 'Keynote: '
  print 'Mark: '
  
  print '\n'
#--------------------------------------------------------------------------
def TabGraphics(theMaterial):
  print '+----------------+'
  print '| TAB - Graphics |'
  print '+----------------+'
  print 'Shading'
  print 'Use Render Appearance: ' + theMaterial.UseRenderAppearanceForShading.ToString()
  print 'Color: ' + GetRGB(theMaterial.Color)
  print 'Transparency: ' + theMaterial.Transparency.ToString()
  
  GetPatterns(theMaterial)
#--------------------------------------------------------------------------
def TabAppearance(theMaterial):
  pass
#--------------------------------------------------------------------------
theMaterials = GetAllMaterials()
theMaterialAssets = GetAllAppearanceAssets()

#for aMaterial in theMaterials: print aMaterial.Name
#for aMaterialAsset in theMaterialAssets: print aMaterialAsset.Name

mat = theMaterials[3]
ReportMaterial(mat)
