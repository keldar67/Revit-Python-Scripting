#========================================================================#
#      _____               __                            
#      \_   \__ _ _ __     \ \  __ _ _ __ ___   ___  ___ 
#       / /\/ _` | '_ \     \ \/ _` | '_ ` _ \ / _ \/ __|
#    /\/ /_| (_| | | | | /\_/ / (_| | | | | | |  __/\__ \
#    \____/ \__,_|_| |_| \___/ \__,_|_| |_| |_|\___||___/
#
#
#  The Script looks for Revit Links then looks for the workset that the 
#  link is in and reports the results to the user
#
#  December 2018
#
#========================================================================#
#------------------------------------------------------------------------#
def GetAllLinks():
  theLinks = (
    FilteredElementCollector(doc)
    .OfCategory(BuiltInCategory.OST_RvtLinks)
    #Only Link Types, NOT a Nested Link
    .Where(lambda link: (RevitLinkInstance == type(link)))
    .OrderBy(lambda link: Element.Name.GetValue(link))
    )
    
  return theLinks.ToList()
#------------------------------------------------------------------------#
def GetLinkName(aLink):
  #return [x.strip() for x in Element.Name.GetValue(aLink).split(':')]
  return Element.Name.GetValue(aLink)
#------------------------------------------------------------------------#
def main()""
	theLinks = GetAllLinks()
	wst = doc.GetWorksetTable()

	for aLink in theLinks:
	  linkname = GetLinkName(aLink)
	  wsetname = wst.GetWorkset(aLink.WorksetId).Name
	  print linkname + '\t\t' + wsetname
	  #print 
	  #print 50 * '-'
#------------------------------------------------------------------------#
if __name__ == '__main__': main()