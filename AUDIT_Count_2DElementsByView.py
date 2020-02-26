#========================================================================#
#      _____               __                            
#      \_   \__ _ _ __     \ \  __ _ _ __ ___   ___  ___ 
#       / /\/ _` | '_ \     \ \/ _` | '_ ` _ \ / _ \/ __|
#    /\/ /_| (_| | | | | /\_/ / (_| | | | | | |  __/\__ \
#    \____/ \__,_|_| |_| \___/ \__,_|_| |_| |_|\___||___/
#
#
#  The Script identifies 2D Elements in Views, and lists the views 
#  ordered by the Total 2D Element
#  
#  2D Element Considered are:
#  [1] 2D Detail Lines
#  [2] Filled Regions
#  [3] Masking Regions
#  [4] Text Notes
#
#  Feb 2020
#
#========================================================================#

#----------------------------------------------------
# Constant Valies for indices
#----------------------------------------------------
INDEX_TOTAL = 0
INDEX_DETAILLINES = 1
INDEX_FILLEDREGIONS = 2
INDEX_MASKINGREGIONS = 3
INDEX_TEXTNOTES = 4
#----------------------------------------------------
# Function for sorting by Total 2D Element Count
#----------------------------------------------------
def by_Total(item):
  return item[1][INDEX_TOTAL]
#----------------------------------------------------
#Get the detail Lines
theLines = (
FilteredElementCollector(doc)
.OfCategory(BuiltInCategory.OST_Lines)
)

detailLines = (theLines
.Where(lambda l: 'Yes'.Equals(l.LookupParameter('Detail Line').AsValueString()))
)
#----------------------------------------------------
#Get the FilledRegions & Masking Regions
Regions = (
FilteredElementCollector(doc)
.OfCategory(BuiltInCategory.OST_DetailComponents)
.Where(lambda fr: FilledRegion == type(fr))
)

Masking = Regions.Where(lambda fr: 'Masking Region'.Equals(fr.LookupParameter('Type Name').Element.Name))
Filled = Regions.Where(lambda fr: 'Detail Filled Region'.Equals(fr.LookupParameter('Type Name').Element.Name))
#----------------------------------------------------
#Get the 2D Text Notes
TextNotes = (
FilteredElementCollector(doc)
.OfCategory(BuiltInCategory.OST_TextNotes)
)
#----------------------------------------------------

theViews = {}

#Count the 2D Detail Lines
for dl in detailLines:
  viewId = dl.OwnerViewId
  if not viewId in theViews:
    #Add the View to the dict and set the line count to 1
    theViews.Add(viewId,[0,1,0,0,0])
  else:
    # Increment the count of lines for this view
    #Index [INDEX_DETAILINES] = 2D Lines
    theViews[viewId][INDEX_DETAILLINES] += 1
    
#Overlay the Filled Regions
for fr in Filled:
  viewId = fr.OwnerViewId
  if not viewId in theViews:
    #Add the View to the dict and set the Filled Region count to 1
    theViews.Add(viewId,[0,0,1,0,0])
  else:
    # Increment the count of Filled Regions for this view
    #Index [INDEX_FILLEDREGIONS] = Filled Regions
    theViews[viewId][INDEX_FILLEDREGIONS] += 1

#Overlay the Filled Regions
for mr in Masking:
  viewId = mr.OwnerViewId
  if not viewId in theViews:
    #Add the View to the dict and set the Filled Region count to 1
    theViews.Add(viewId,[0,0,0,1,0])
  else:
    # Increment the count of Filled Regions for this view
    #Index [INDEX_MASKINGREGIONS] = Masking Regions
    theViews[viewId][INDEX_MASKINGREGIONS] += 1
    
#Overlay 2D Text
for tx in TextNotes:
  viewId = tx.OwnerViewId
  if not viewId in theViews:
    #Add the View to the dict and set the Filled Region count to 1
    theViews.Add(viewId,[0,0,0,0,1])
  else:
    # Increment the count of Filled Regions for this view
    #Index [INDEX_MASKINGREGIONS] = Masking Regions
    theViews[viewId][INDEX_MASKINGREGIONS] += 1

#Sum up all of the 2D elements into the total of each dict element
for aView in theViews:
  theViews[aView][INDEX_TOTAL] = (theViews[aView][INDEX_DETAILLINES] + theViews[aView][INDEX_FILLEDREGIONS] + theViews[aView][INDEX_MASKINGREGIONS] + theViews[aView][INDEX_TEXTNOTES])

#Sort the dictionary by Total 2D Element Most to Fewest
sortedViews = sorted(theViews, key=lambda v: theViews[v][INDEX_TOTAL], reverse=True)

# Print the Table Header
print '+---------+---------+---------+---------+---------+-----------+---------------------------------------------------+'
print '|TOTAL 2D |  DETAL  | FILLED  | MASKING |   TEXT  |  VIEWID   |  VIEW NAME'
print '|ELEMENTS |  LINES  | REGIONS | REGIONS |   NOTES |           |'
print '+---------+---------+---------+---------+---------+-----------+---------------------------------------------------+'

for aView in sortedViews:
  #Convert the numbers to justified strings
  theTotal = theViews[aView][INDEX_TOTAL].ToString().rjust(8)
  detlines = theViews[aView][INDEX_DETAILLINES].ToString().rjust(8)
  filledrg = theViews[aView][INDEX_FILLEDREGIONS].ToString().rjust(8)
  maskingr = theViews[aView][INDEX_MASKINGREGIONS].ToString().rjust(8)
  textnote = theViews[aView][INDEX_TEXTNOTES].ToString().rjust(8)
  viewId = aView.ToString().rjust(10)
  viewname = Element.Name.GetValue(doc.GetElement(aView))
  
  #Print each data row for each view
  print '|' + theTotal + ' |' + detlines + ' |' + filledrg + ' |' + maskingr + ' |' + textnote + ' |' + viewId + ' | ' + viewname

#Close the bottom of the table output
print '+---------+---------+---------+---------+---------+-----------+---------------------------------------------------+'