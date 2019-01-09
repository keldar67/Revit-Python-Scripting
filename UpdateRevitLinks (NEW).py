#========================================================================#
#      _____               __                            
#      \_   \__ _ _ __     \ \  __ _ _ __ ___   ___  ___ 
#       / /\/ _` | '_ \     \ \/ _` | '_ ` _ \ / _ \/ __|
#    /\/ /_| (_| | | | | /\_/ / (_| | | | | | |  __/\__ \
#    \____/ \__,_|_| |_| \___/ \__,_|_| |_| |_|\___||___/
#
#  Automation of Revit Link Updating initally written for QQT
#
#  The Script looks for Revit Links then looks at the folder they came 
#  from to see if there is a higher numbered revision and if so then
#  it will swap to that revision.
#
#  January 2019
#
#========================================================================#
import os
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
def GetLinkFolderPath(aLink):
  thePath = ''
  #Get the External Reference
  er = aLink.GetExternalFileReference()
  #Make sure it isn't Null
  if not(er):
    print GetLinkName(aLink)
  else:
    #Get the Model Path
    mp = er.GetPath()
    #Convert the Model Path to a human readable format
    #Also convert relative paths to absolute paths
    modelpath = ModelPathUtils.ConvertModelPathToUserVisiblePath(mp)
    thePath = os.path.dirname(os.path.abspath(modelpath))
    
  return thePath
#------------------------------------------------------------------------# 
def GetRevNumberFromFileName(filename):
  linkinfo = filename.split('-')
  if 'RVT' in linkinfo:
    # return the item in the list after 'RVT'
    # which should be the revision number.
    revnumber = int(linkinfo[linkinfo.IndexOf('RVT')+1])
  else:
    revnumber = 0
    
  return revnumber
#------------------------------------------------------------------------# 
def GetLatestRevisionFromFolder(aLink):
  #Get the path that the Link comes from
  folderpath = GetLinkFolderPath(aLink)
  filename = Element.Name.GetValue(aLink)
  #Only check if the file is from the Revit Links Folder
  if folderpath.Contains('Revit Links'):
    
    #Get the start of the filename up to the Revision
    #so that we can filter files we are interested in.
    filestart = filename[:filename.find('-RVT-')]
    
    # list of Revit files in the folder that match
    # both the start of the filename and end with .rvt
    filenames = [fn for fn in os.listdir(folderpath)
                 if fn.startswith(filestart)]
   
    highest = 0
    #print folderpath
    #If more than one file... loop through and find highest revision
    for afile in filenames:
      num = GetRevNumberFromFileName(afile)
      if num > highest:
        highest = num
        theFile = afile
      else:
        #We have a match
        if num == highest:
          theFile = afile
    #Return an updated File Path of a higher Revision    
    return (folderpath,theFile)    
  else:
    #Return an empty string if not from 'Revit Links Folder'.
    return '' 
    
#------------------------------------------------------------------------#
def GetLinkedDocuments():
  theDocuments = {}
  
  for aDoc in doc.Application.Documents:
    theDocuments.update({aDoc.Title: aDoc})
    
  return theDocuments
#------------------------------------------------------------------------#
def GetLinkedDocumentDoc(theDocuments, aLinkName):
  
  #remove the ".rvt"
  aLinkName = aLinkName[:aLinkName.find('.rvt')]
  
  #Check that the document is in the open documents (ie a Link)
  if theDocuments.ContainsKey(aLinkName):
    #---------print 'File: ' + aLinkName + ' is in the Dictionary'
    linkdoc = theDocuments[aLinkName]
  else:
    linkdoc = None     
  return linkdoc
#------------------------------------------------------------------------#
def GetClosedWorksetIds(linkdoc):
  #Get the Worksets
  theWorksets = (
    FilteredWorksetCollector(linkdoc)
    .Where(lambda ws: ws.Kind == WorksetKind.UserWorkset)
    )
    
  ClosedWorksets = []
  
  for aWorkset in theWorksets:
    if not(aWorkset.IsOpen):
      ClosedWorksets.Add(aWorkset.Id)
      
  #Return the list of Ids    
  return ClosedWorksets
#------------------------------------------------------------------------#
def LogListClosedWorksets(linkdoc, wslist):
  
  wst = linkdoc.GetWorksetTable()
  
  wlist = ''
  #Print the list of Closed Worksets to the Log
  for w in wslist:
    wlist = wlist +  '\n  [-] ' + wst.GetWorkset(w).Name
  
  return wlist
#------------------------------------------------------------------------#

#------------------------------------------------------------------------#
NotWorksharedLinks = []
LogSeparator = '+------------------------------------------------------------------------+'
#Get All of the current open documents
theDocuments = GetLinkedDocuments()

#for aDocument in theDocuments:
#  print aDocument
#  print theDocuments[aDocument]

# Get All of the Links (LinkTypes Only)
theLinks = GetAllLinks()

#Create a Log Element for each link
linklog = ''
linklog = linklog + '\n' + LogSeparator

#For Each of the Links:
for aLink in theLinks:
  theLinkPath = GetLinkFolderPath(aLink)
  theLinkName = GetLinkName(aLink)
  
  
  #linklog = linklog + '\n'
  #linklog = linklog + '\n'
  
  if '8.0 Revit Links' in theLinkPath:
  
    linklog = linklog + '\nLink Name = ' + theLinkName
    linklog = linklog + '\nLink Path = ' + theLinkPath
    
    #Check to see if this link is loaded so we can re-instate this status
    isloaded = aLink.IsLoaded(doc,aLink.Id)
    
    #Get the Current Revision of this link
    theLinkCurrentRev = GetRevNumberFromFileName(theLinkName)
    
    #Get the Highest Revision Available
    newLinkPath, newLinkName = GetLatestRevisionFromFolder(aLink)
    
    #Get the Potential New Revision Number
    NewRevision = GetRevNumberFromFileName(newLinkName)
    
    if theLinkCurrentRev.Equals(NewRevision):
      #No Relinking is required.
      linklog = linklog + '\nFile: ' + theLinkName + ' is already up to date at Rev ' + theLinkCurrentRev.ToString()
    else:
      #We need to relink from the newer revision.
      linklog = linklog + '\nNeed to update from Rev ' + theLinkCurrentRev.ToString() + ' to Rev ' + NewRevision.ToString()
      
      linkdoc = GetLinkedDocumentDoc(theDocuments, theLinkName)
      
      #make Sure we got a valid document back.
      if linkdoc:
        if linkdoc.IsWorkshared:
          #If the link is Workshared we need to make sure we match any closed Worksets
          #--------print 'Getting the Workset Status of the link:' + linkdoc.Title
          #Get the List of Closed Worksets
          closedWS = GetClosedWorksetIds(linkdoc)
          wc = WorksetConfiguration()
          wc.Close(closedWS)
          #worksetinfo(linkdoc)
          linklog = linklog + '\nClosed Worksets as follows:'
          linklog = linklog + LogListClosedWorksets(linkdoc,closedWS)
        else:
          NotWorksharedLinks.Add(GetLinkName(aLink))
      else:
        linklog - linklog + '\nlinkDoc Not Found'       
    
    #print 'PATH - ' + theLinkPath
    #print 'NAME - ' + theLinkName
    #print 'CREV - ' + theLinkCurrentRev.ToString()
    #print '-' * 50
    #print 'NewPATH - ' + newLinkPath
    #print 'newNAME - ' + newLinkName
    #print 'NRev - ' + NewRevision.ToString()
    #print '-' * 75
    
    linklog = linklog + '\n' + LogSeparator
    
  else:
    pass
    #print '... not a Revit Link'

#Print the Link Log to the Screen
print linklog  


#If the Link was unloaded prior to being up-revved - reistate.
  #if not isloaded:
  #  aLink.Unload('Need to figure out how to use this method)
if NotWorksharedLinks.Count > 0:
  print '\nThe Following Links are not workshared...!!\n'
  for nwl in NotWorksharedLinks:
    print nwl



