#------------------------------------------------------------------------#
def GetAllLinks():
  theLinks = (
    FilteredElementCollector(doc)
    .OfCategory(BuiltInCategory.OST_RvtLinks)
    #Only Link Types, NOT a Nested Link
    .Where(lambda link: (RevitLinkType == type(link)) and not(link.IsNestedLink))
    )
    
  return theLinks.ToList()
#------------------------------------------------------------------------#
def GetLinkName(aLink):
  #return [x.strip() for x in Element.Name.GetValue(aLink).split(':')]
  return Element.Name.GetValue(aLink)
#------------------------------------------------------------------------#  
def GetLinkPath(aLink):
  er = aLink.GetExternalFileReference()
  mp = er.GetPath()
  thePath = ModelPathUtils.ConvertModelPathToUserVisiblePath(mp)
  
  return thePath
#------------------------------------------------------------------------#
def GetLinkModelPath(aLink):
  er = aLink.GetExternalFileReference()
  mp = er.GetPath()
  
  return mp
#------------------------------------------------------------------------#
def worksetinfo(linkdoc):
  #linkdoc = aLink.Document
  #Get the Worksets
  theWorksets = (
    FilteredWorksetCollector(linkdoc)
    .Where(lambda ws: ws.Kind == WorksetKind.UserWorkset)
    )
  
  closedWorksets = []
  print linkdoc.Title
  for aWorkset in theWorksets:
    if aWorkset.IsOpen:
      print '  [o] - ' + aWorkset.Name
    else:
      closedWorksets.Add(aWorkset)
      print '  [-] - ' + aWorkset.Name
#------------------------------------------------------------------------#
def GetLinkedDocuments():
  theDocuments = {}
  
  for aDoc in doc.Application.Documents:
    theDocuments.update({aDoc.Title: aDoc})
  
  return theDocuments
#------------------------------------------------------------------------#
def GetLinkedWorksetStatus():
  #Get the Links - Document
  ldoc = aLink.Document
  #Get it's Workset Table
  lwst = ldoc.GetWorksetTable()
  #Just as a test Get the Links Active Workset
  laws = lwst.GetWorkset(lwst.GetActiveWorksetId())
  #Test to see if that Workset is open
  laws.IsOpen
 
  #Read this - https://forums.autodesk.com/t5/revit-api-forum/manage-worksets-of-a-link/td-p/6412881
  
  theWorksets = FilteredWorksetCollector(ldoc)
  
  for aWorkset in theWorksets:
    if aWorkset.Kind == WorksetKind.UserWorkset:
      print aWorkset.Name

#------------------------------------------------------------------------#
theLinks = GetAllLinks()
#aLink = theLinks[0]
#mp = GetLinkModelPath(aLink)
#wsp = WorksharingUtils.GetUserWorksetInfo(mp)
#for w in wsp: print w.Name
NotWorkshared = []
theDocuments = GetLinkedDocuments()

for aLink in theLinks:
  linkname = GetLinkName(aLink)
  if linkname in theDocuments.Keys:
    linkdoc = theDocuments[linkname]
  if linkdoc.IsWorkshared:
    worksetinfo(linkdoc)
  else:
    NotWorkshared.Add(linkdoc.Title)
    
if NotWorkshared.Count > 0:
  print 'The Following Links are not workshared...!!'
  for nws in NotWorkshared:
    print nws