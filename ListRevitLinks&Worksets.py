
#------------------------------------------------------------------------#
def GetAllLinks():
  theLinks = (
    FilteredElementCollector(doc)
    .OfCategory(BuiltInCategory.OST_RvtLinks)
    #Only Link Types, NOT a Nested Link
    .Where(lambda link: (RevitLinkType == type(link)) and not(link.IsNestedLink))
    .OrderBy(lambda link: Element.Name.GetValue(link))
    )
    
  return theLinks.ToList()
#------------------------------------------------------------------------#
def GetLinkName(aLink):
  #return [x.strip() for x in Element.Name.GetValue(aLink).split(':')]
  return Element.Name.GetValue(aLink)
#------------------------------------------------------------------------#

theLinks = GetAllLinks()
wst = doc.GetWorksetTable()

for aLink in theLinks:
  linkname = GetLinkName(aLink)
  wsetname = wst.GetWorkset(aLink.WorksetId).Name
  print linkname + '\t\t' + wsetname
  #print 
  #print 50 * '-'