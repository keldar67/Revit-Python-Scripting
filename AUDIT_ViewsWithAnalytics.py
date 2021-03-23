#========================================================================#
#      _____               __                            
#      \_   \__ _ _ __     \ \  __ _ _ __ ___   ___  ___ 
#       / /\/ _` | '_ \     \ \/ _` | '_ ` _ \ / _ \/ __|
#    /\/ /_| (_| | | | | /\_/ / (_| | | | | | |  __/\__ \
#    \____/ \__,_|_| |_| \___/ \__,_|_| |_| |_|\___||___/
#
#
#  Identifies Views (with No Template) where the Analytics are Enabled
#  Then also shows all of the View Templates that have the Analytics
#  enabled.
#
#  July 2020
#
#========================================================================#
allViews = (
FilteredElementCollector(doc)
.OfClass(View)
.OrderBy(lambda f: f.ViewType)
)

print '+-------------------------------------------------------------+'
print '| Views with Analytics Enabled and No Template                |'
print '+-------------------------------------------------------------+'
for aView in allViews:
  # Only show Views without a View Template
  if not(aView.ViewTemplateId == ElementId.InvalidElementId):
    # Filter just Views without templates that have Analytics enabled
    if aView.AreAnalyticalModelCategoriesHidden:
      print aView.Id.ToString().rjust(10) + ' | ' + aView.ViewName
    #print aView.ViewType

allTemplates = (
FilteredElementCollector(doc)
.OfCategory(BuiltInCategory.OST_Views)
.Where(lambda v: v.IsTemplate)
)

print '+-------------------------------------------------------------+'
print '| View Templates with Analytics Enabled                       |'
print '+-------------------------------------------------------------+'
for aTemplate in allTemplates:
  if aTemplate.AreAnalyticalModelCategoriesHidden:
      print aTemplate.Id.ToString().rjust(10) + ' | ' + aTemplate.ViewName
print '+-------------------------------------------------------------+'
#v = doc.ActiveView
#print v.AreAnalyticalModelCategoriesHidden
