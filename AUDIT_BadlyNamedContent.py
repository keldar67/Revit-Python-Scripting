#========================================================================#
#      _____               __                            
#      \_   \__ _ _ __     \ \  __ _ _ __ ___   ___  ___ 
#       / /\/ _` | '_ \     \ \/ _` | '_ ` _ \ / _ \/ __|
#    /\/ /_| (_| | | | | /\_/ / (_| | | | | | |  __/\__ \
#    \____/ \__,_|_| |_| \___/ \__,_|_| |_| |_|\___||___/
#
#
#  The Script identifies Badly Named Families or Groups 
#  in the model and lists them
#
#  June 2020
#
#========================================================================#
fams = (
FilteredElementCollector(doc)
.OfClass(Family)
#.OrderBy(lambda f: f.Category.Name)
.Where(lambda f: f.IsEditable and f.Name.StartsWith('Family'))
.ToList()
)


DGroups = (
FilteredElementCollector(doc)
.OfCategory(BuiltInCategory.OST_IOSDetailGroups)
.Where(lambda dg: Element.Name.GetValue(dg).StartsWith('Group') and type(dg) == GroupType)
)


MGroups = (
FilteredElementCollector(doc)
.OfCategory(BuiltInCategory.OST_IOSModelGroups)
.Where(lambda mg: Element.Name.GetValue(mg).StartsWith('Group') and type(mg) == GroupType)
)

print '+-------------------------------------------------+'
print '| Badly Named Families                            |'
print '+--------------------------+----------------------+'
for fam in fams: 
  thecat = fam.FamilyCategory.Name.ljust(24)
  theName = fam.Name.rjust(20)
  print '| ' + thecat + ' | ' + theName + ' |'
print '+--------------------------+----------------------+'
print '| Badly Named Detail Groups                       |'
print '+-------------------------------------------------+'
for dg in DGroups:
  theName = Element.Name.GetValue(dg).ljust(47)
  print '| ' + theName + ' |'
print '+-------------------------------------------------+'
print '| Badly Named Model Groups                        |'
print '+-------------------------------------------------+'
for mg in MGroups:
  theName = Element.Name.GetValue(mg).ljust(47)
  print '| ' + theName + ' |'
print '+-------------------------------------------------+'  
  
  