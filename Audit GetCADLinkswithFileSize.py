import os

#-------------------------------------------------------------------------
def extRefToPath(link):
  extref = transData.GetLastSavedReferenceData(aLink)
  path = ModelPathUtils.ConvertModelPathToUserVisiblePath(extref.GetPath())
  return path
#-------------------------------------------------------------------------  

# Get the Model Path of the Current Document
mp = doc.GetWorksharingCentralModelPath()

# Then convert that Model Path to a Human Readable format
path = ModelPathUtils.ConvertModelPathToUserVisiblePath(mp)  

# Get the TransmissionData from the current Document
transData = TransmissionData.ReadTransmissionData(mp)

# Grab all of the External File References from the 
# current Documents Transmission Data
linkIDs = transData.GetAllExternalFileReferenceIds()
separator = '+-----+----------------------------------------------------+----------+'
totalsize = 0.0
count = 0
CADLinks = []
#Loop through all of the CAD Links and get the information
for aLink in linkIDs:
  theName = Element.Name.GetValue(doc.GetElement(aLink))
  if theName.EndsWith('.dwg'):
    thePath = extRefToPath(aLink)
    if os.path.exists(thePath):
      
      theSize = os.path.getsize(thePath) / (1024.0 * 1024.0)
      
      
      # Add the dwg link to the new list
      CADLinks.Add([thePath,theName,theSize])
      
      # Add the size to the total
      totalsize += theSize

print len(CADLinks)

# Now loop through the derived list of CAD Links and print them out
for aLink in CADLinks:
  count += 1
  strCount = "{:03d}".format(count)
  strSize = "{:.3f}".format(aLink[2])
  # Then output it tabulated
  print separator
  print '| ' + strCount + ' | ' + aLink[1].ljust(50) + ' | ' + strSize.rjust(8) + ' | ' + aLink[0]
  
  
  #print theName
  #print thePath
  #print "{:.3f}".format(float(theSize))
  #print 75 * '-'
print separator      
print '|       ' + 'Total'.rjust(50) + ' | ' + "{:.3f}".format(totalsize).rjust(8) + ' | '
print separator
