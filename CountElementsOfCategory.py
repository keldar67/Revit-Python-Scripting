#############################################
#         UNCOMMENT JUST ONE
#############################################
#bic = BuiltInCategory.OST_TextNotes
#bic = BuiltInCategory.OST_SpotElevations
#bic = BuiltInCategory.OST_Viewports
#bic = BuiltInCategory.OST_Views
bic = BuiltInCategory.OST_Grids
#############################################

theThings = (
FilteredElementCollector(doc)
.OfCategory(bic)
)

count = theThings.Count().ToString()

print 'There are ' + count + ' Elements in the model'