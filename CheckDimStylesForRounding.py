#========================================================================#
#      _____               __                            
#      \_   \__ _ _ __     \ \  __ _ _ __ ___   ___  ___ 
#       / /\/ _` | '_ \     \ \/ _` | '_ ` _ \ / _ \/ __|
#    /\/ /_| (_| | | | | /\_/ / (_| | | | | | |  __/\__ \
#    \____/ \__,_|_| |_| \___/ \__,_|_| |_| |_|\___||___/
#
#
#  The Script looks at all of the DimensionStyles to check if they have 
#  had rounding applied
#  The first filter selects only Dimension Styles that are not set to 
#  Use Default Settings. It is assumed that Default Settings are not set
#  to use rounding.
#
#  March 2019
#
#========================================================================#

theDimStyles = (
  FilteredElementCollector(doc)
  .OfClass(DimensionType)
  .Where(lambda ds: ds.GetUnitsFormatOptions().UseDefault.Equals(False))
  )

for aDimStyle in theDimStyles:
  fo = aDimStyle.GetUnitsFormatOptions()
  
  if fo.RoundingMethod.Equals(RoundingMethod.Nearest):
    DSName = Element.Name.GetValue(aDimStyle)
    print DSName + " is rounded to " + str(fo.Accuracy) + " (" + fo.DisplayUnits.ToString() + ") "
  
  