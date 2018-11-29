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
#  November 2018
#
#========================================================================#
import os

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
    print Element.Name.GetValue(aLink)
  else:
    #Get the Model Path
    mp = er.GetPath()
    #Convert the Model Path to a human readable format
    #Also convert relative paths to absolute paths
    thePath = os.path.dirname(os.path.abspath(ModelPathUtils.ConvertModelPathToUserVisiblePath(mp)))
    
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
    #Return an updated File Path of a higher Revision    
    return (folderpath,theFile)    
  else:
    #Return an empty string if not from 'Revit Links Folder'.
    return '' 
    
#------------------------------------------------------------------------#
theLinks = (
  FilteredElementCollector(doc)
  .OfCategory(BuiltInCategory.OST_RvtLinks)
  #Only Link Types, NOT Link Instances
  .Where(lambda link: RevitLinkType == type(link))
  )
  
RevitLinks = []
LatestRevisions = []

for aLink in theLinks:
  theFolder = GetLinkFolderPath(aLink)
  # Filter down the selection of links to only those in the
  # Revit Links folder... We aren't interested in any others.
  if 'Revit Links' in theFolder:
    current = (theFolder, Element.Name.GetValue(aLink))
    latest = GetLatestRevisionFromFolder(aLink)
    RevitLinks.Add(current)
    LatestRevisions.Add(latest)
    if GetRevNumberFromFileName(latest[1]) > GetRevNumberFromFileName(current[1]):
      print 'Need to swap ' + GetLinkName(aLink) + ' Rev ' + str(GetRevNumberFromFileName(current[1])) + ' for ' + str(GetRevNumberFromFileName(latest[1]))
      print 50*'-'
      newpath = '\\'.join(latest)
      print 'newpath: ' + newpath
      #Creat a Revit Readable File Reference from the file path.
      modelpath = ModelPathUtils.ConvertUserVisiblePathToModelPath(newpath)
      try:
        reloadResults = aLink.LoadFrom(modelpath, WorksetConfiguration())
      except Exception as e:
        print e.message
      
      print reloadResults.LoadResult
    
for rl, lr in zip(RevitLinks, LatestRevisions):
  print rl[0]
  print rl[1]
  print lr[0]
  print lr[1]
  print 50*'-'
