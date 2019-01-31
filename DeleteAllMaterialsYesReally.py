#========================================================================#
#      _____               __                            
#      \_   \__ _ _ __     \ \  __ _ _ __ ___   ___  ___ 
#       / /\/ _` | '_ \     \ \/ _` | '_ ` _ \ / _ \/ __|
#    /\/ /_| (_| | | | | /\_/ / (_| | | | | | |  __/\__ \
#    \____/ \__,_|_| |_| \___/ \__,_|_| |_| |_|\___||___/
#
#
#  This script removes all materials and material assets from a model. 
#
#  WARNING... THIS WAS WRITTEN FOR A VERY SPECIFIC PURPOSE. ONLY USE IF 
#             YOU WANT TO PERMANENTLY DELETE ALL MATERIALS AND APPEARANCE
#             ASSETS.  
#
#  December 2018
#
#========================================================================#
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