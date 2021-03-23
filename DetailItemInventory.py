#========================================================================#
#      _____               __                            
#      \_   \__ _ _ __     \ \  __ _ _ __ ___   ___  ___ 
#       / /\/ _` | '_ \     \ \/ _` | '_ ` _ \ / _ \/ __|
#    /\/ /_| (_| | | | | /\_/ / (_| | | | | | |  __/\__ \
#    \____/ \__,_|_| |_| \___/ \__,_|_| |_| |_|\___||___/
#
#
#  The Script identifies Detail Items and lists
#   - Families
#   - Types
#   - Instance counts of each type
#  
#
#  Nov 2020
#
#========================================================================#

PrintToExcel = False

def PrintResultsToExcel(families):
  pass
  #Function to be written here to parse results out to Excel.

theDetailItemFamilies = (
  FilteredElementCollector(doc)
  .WherePasses(ElementClassFilter(FamilySymbol))
  .WherePasses(ElementCategoryFilter(BuiltInCategory.OST_DetailComponents))
  .GroupBy(lambda e: e.Family.Name)
  #.OrderBy(lambda e: e.Family.Name)
  .ToDictionary(lambda e: e.Key, lambda e: e.ToList())
  )
  
for aDetailItemFamily in sorted(theDetailItemFamilies):
  #Grab The Family Name
  FamName = aDetailItemFamily.Key
  print '+---' + '-'*50 + '-+-' + '-' *6 + '-+'
  print '| ' + FamName.ljust(56+5) + ' |'
  print '+---' + '-'*50 + '-+-' + '-' *6 + '-+'
  #The Grab each Family Type Name
  for adi in theDetailItemFamilies[aDetailItemFamily.Key]:
    FamTypeName = Element.Name.GetValue(adi)
    
    #Then check to see how many instances of each type are placed in the model.
    theFamilyInstances = (
    FilteredElementCollector(doc)
    .WherePasses(ElementClassFilter(FamilyInstance))
    .WherePasses(ElementCategoryFilter(BuiltInCategory.OST_DetailComponents))
    .Where(lambda f: Element.Name.GetValue(f.Symbol) == Element.Name.GetValue(adi))
    )
    
    FamTypeCount = theFamilyInstances.Count().ToString()
    print '| - ' + FamTypeName.ljust(50) + ' | ' + FamTypeCount.rjust(6) + ' |'
    
print '+---' + '-'*50 + '-+-' + '-' *6 + '-+'