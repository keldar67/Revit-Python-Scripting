#========================================================================#
#      _____               __                            
#      \_   \__ _ _ __     \ \  __ _ _ __ ___   ___  ___ 
#       / /\/ _` | '_ \     \ \/ _` | '_ ` _ \ / _ \/ __|
#    /\/ /_| (_| | | | | /\_/ / (_| | | | | | |  __/\__ \
#    \____/ \__,_|_| |_| \___/ \__,_|_| |_| |_|\___||___/
#
#
#  The Script measures the size of the active model as well as all of 
#  the linked models.
#  It produces stat information on how much RAM is required to
#  effectively work in this full model environment based on
#  20 x size of compacted size of the active  model central model.
#  plus
#  1 x the sum of all linked models
#
#  Ref: https://knowledge.autodesk.com/support/revit-products/learn-explore/caas/CloudHelp/cloudhelp/2019/ENU/Revit-Customize/files/GUID-C395AAC8-B5E2-40A5-8B48-1BFEEA9116D6-htm.html
#  Ref: https://knowledge.autodesk.com/support/revit-products/troubleshooting/caas/sfdcarticles/sfdcarticles/Revit-How-to-calculate-required-RAM-specific-to-a-project-size.html
#
#  February 2019
#
#========================================================================#
import os
#------------------------------------------------------------------------#
def SizeInMegaBytes(size):
  MB = 1048576
  return size / MB
#------------------------------------------------------------------------#
def SizeInKiloBytes(size):
  KB = 1024
  return size / KB
#------------------------------------------------------------------------#
def GetModelSize(theDoc):
  mp = theDoc.GetWorksharingCentralModelPath()
  thePath = ModelPathUtils.ConvertModelPathToUserVisiblePath(mp)
  statinfo = os.stat(thePath)
  
  return statinfo.st_size
#------------------------------------------------------------------------#
def GetLinkSize(aLink):
  thePath = ''
  #Get the External Reference
  er = aLink.GetExternalFileReference()
  #Make sure it isn't Null
  if not(er):
    print Element.Name.GetValue(aLink)
  else:
    #Get the Model Path
    mp = er.GetPath()
    #Convert the Model Path to a human readable format
    #Also convert relative paths to absolute paths
    thePath = ModelPathUtils.ConvertModelPathToUserVisiblePath(mp)
    
  statinfo = os.stat(thePath)
  
  return statinfo.st_size
#------------------------------------------------------------------------#
def GetCentralModelName():
  return doc.Title[:doc.Title.LastIndexOf('_')] + '.rvt'
#------------------------------------------------------------------------#
def GetNameColumnWidth(theLinkTypes):
  docTitle = GetCentralModelName()
  NameLength = len(docTitle)
  
  for aLink in theLinkTypes:
    linkName = Element.Name.GetValue(aLink)
    # If the Link Name eis longer that what we already have then 
    # we have a new maximum
    if len(linkName) > NameLength: NameLength = len(linkName)
  
  
  return NameLength
#------------------------------------------------------------------------#
def GetIdColumnWidth(theLinkTypes):
  idLength = 0
  for aLink in theLinkTypes:
    if len(aLink.Id.ToString()) > idLength: idLength = len(aLink.Id.ToString()) 
    
  return idLength
#------------------------------------------------------------------------#
documents = doc.Application.Documents
TopLevelLinks = []
NestedLinks = []

RamSize = 0L

theLinkTypes = (
  FilteredElementCollector(doc)
  .OfCategory(BuiltInCategory.OST_RvtLinks)
  .Where(lambda rl: RevitLinkType ==type(rl))
  .OrderBy(lambda rl: Element.Name.GetValue(rl))
  )

for aLink in theLinkTypes:
  x = '+' if aLink.IsNestedLink else 'o'
  pid = aLink.GetParentId().ToString() if aLink.IsNestedLink else ''
  
  #Sort Top Level and Nested Links
  if aLink.IsNestedLink:
    NestedLinks.append(aLink)
  else:
    TopLevelLinks.append(aLink)
    
  #Get Link Size
  linksize = GetLinkSize(aLink)
  
  RamSize += linksize
  
  print '[' + x + '][' + aLink.Id.ToString() + '] ' + Element.Name.GetValue(aLink) + ' [' + SizeInKiloBytes(linksize).ToString() + ']'

print 'N° of Links: ' + theLinkTypes.Count().ToString()

activemodelsize = GetModelSize(doc)
RamRequired = 20* activemodelsize

#Get formatting for tabulating the output
ColIdWidth = GetIdColumnWidth(theLinkTypes)
ColNameWidth = GetNameColumnWidth(theLinkTypes)

print 'Id  : ' + ColIdWidth.ToString()
print 'Name: ' + ColNameWidth.ToString()

print 'Model Size (MB)    = ' + SizeInKiloBytes(activemodelsize).ToString()
print 'Min RAM Required   = ' + SizeInKiloBytes(RamRequired).ToString()
print 'Overall Link Size  = ' + SizeInKiloBytes(RamSize).ToString()
print '+----------------------------+'
print 'Total Ram Required = ' + SizeInKiloBytes(RamSize + RamRequired).ToString()

#------------------------------------------------------------------------#
def Horizontal():
  print '+' + '-' * (ColIdWidth + 2) + '+' + '-' * (ColNameWidth + 2) + '+'
#------------------------------------------------------------------------#
def HorizontalBlank():
  print '|' + ' ' * (ColIdWidth + 2) + '|' + ' ' * (ColNameWidth + 2) + '|'
#------------------------------------------------------------------------#
Horizontal()

# Print Active Model as Title
print '| ' + 'Id'.center(ColIdWidth) + ' | ' + GetCentralModelName().ljust(ColNameWidth) + ' |'

Horizontal()

# Print Linked Models
for l in TopLevelLinks:
  id = l.Id.ToString()
  name = Element.Name.GetValue(l)
  print '| ' + id.rjust(ColIdWidth) + ' | ' + name.ljust(ColNameWidth) + ' |'

Horizontal()


