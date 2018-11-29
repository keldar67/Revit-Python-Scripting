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
def GetCurrentRevisionLoaded(aLink):
  filename = GetLinkName(aLink)
  return GetRevNumberFromFileName(filename)
#------------------------------------------------------------------------#
def GetRevNumberFromFilePath(filepath):
  filename = os.path.basename(filepath)
  return GetRevNumberFromFileName(filename)
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
    print folderpath
    #If more than one file... loop through and find highest revision
    for afile in filenames:
      num = GetRevNumberFromFileName(afile)
      if num > highest:
        highest = num
        theFile = afile
    #Return an updated File Path of a higher Revision    
    return folderpath + '\\' + theFile    
  else:
    #Return an empty string if not from 'Revit Links Folder'.
    return '' 
    
#------------------------------------------------------------------------#
def main():
  pass
#------------------------------------------------------------------------#
theLinks = (
  FilteredElementCollector(doc)
  .OfCategory(BuiltInCategory.OST_RvtLinks)
  .Where(lambda link: RevitLinkType == type(link))
  )

for aLink in theLinks:
  #Get the Revision Number of the current Link File
  revnumber = GetCurrentRevisionLoaded(aLink)
    
  #Look to see if there is a newer revision (Higher Number of the same file)
  newfile = GetLatestRevisionFromFolder(aLink)
  # Only proceed if we got a file path back
  if newfile:
    newrev = GetRevNumberFromFilePath(newfile)
    if newrev > revnumber:
      #Update the Link Here
      theName = Element.Name.GetValue(aLink)
      print str(newrev) + '\t' + newfile
      print 'Updating ' + theName + ' from Rev ' + str(revnumber) + ' to ' + str(newrev)
      theModelPath = ModelPathUtils.ConvertUserVisiblePathToModelPath(newfile)
      res = aLink.LoadFrom(theModelPath,WorksetConfiguration)
      print res.LoadResults
      
    else: #newfile == revnumber:
      print 'Already Up To Date\t\t[' + str(newrev) + '][' + str(revnumber) + ']'
  
