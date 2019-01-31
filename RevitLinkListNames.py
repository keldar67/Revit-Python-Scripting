#========================================================================#
#      _____               __                            
#      \_   \__ _ _ __     \ \  __ _ _ __ ___   ___  ___ 
#       / /\/ _` | '_ \     \ \/ _` | '_ ` _ \ / _ \/ __|
#    /\/ /_| (_| | | | | /\_/ / (_| | | | | | |  __/\__ \
#    \____/ \__,_|_| |_| \___/ \__,_|_| |_| |_|\___||___/
#
#
#  The Script lists the Revit Links alphabetically 
#  and reports the results to the user
#
#  December 2018
#
#========================================================================#
theLinks = (
  FilteredElementCollector(doc)
  .OfCategory(BuiltInCategory.OST_RvtLinks)
  .OrderBy(lambda n: Element.Name.GetValue(n))
  )

for aLink in theLinks:
  if RevitLinkInstance == type(aLink):
    data = Element.Name.GetValue(aLink).split(':')
    print data[0]