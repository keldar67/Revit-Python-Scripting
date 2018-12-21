#==============================================================#
#      _____               __                            
#      \_   \__ _ _ __     \ \  __ _ _ __ ___   ___  ___ 
#       / /\/ _` | '_ \     \ \/ _` | '_ ` _ \ / _ \/ __|
#    /\/ /_| (_| | | | | /\_/ / (_| | | | | | |  __/\__ \
#    \____/ \__,_|_| |_| \___/ \__,_|_| |_| |_|\___||___/
#
#    Written: December 2018
#
#    Script to automate re-linking  Revit and CAD Links into
#    newly upgraded models to the new 003 Multiplex folder 
#    structure
#
#==============================================================#
import os

projfilesfolder = r'X:\003 - Multiplex\Design\BIM\_Revit\1.0 Project Files\1.0 QQT'
sitefilesfolder = r'X:\003 - Multiplex\Design\BIM\_Revit\1.0 Project Files\2.0 Site'
areafilesfolder = r'X:\003 - Multiplex\Design\BIM\_Revit\1.0 Project Files\4.0 Areas'

BVNProjfiles = {
'AR-MOD-XX-XX-000': os.path.join(sitefilesfolder,'AR-MOD-XX-XX-000-RVT - Model Management.rvt'),
'AR-MOD-XX-XX-001': os.path.join(sitefilesfolder,'AR-MOD-XX-XX-001-RVT - Site.rvt'),
'AR-MOD-XX-XX-002': os.path.join(projfilesfolder,'AR-MOD-XX-XX-002-RVT - Structure.rvt'),
'AR-MOD-XX-XX-003': os.path.join(projfilesfolder,'AR-MOD-XX-XX-003-RVT - Crown Louvers.rvt'),
'AR-MOD-XX-XX-004': os.path.join(projfilesfolder,'AR-MOD-XX-XX-004-RVT - Facade Tower.rvt'),
'AR-MOD-XX-XX-005': os.path.join(projfilesfolder,'AR-MOD-XX-XX-005-RVT - Basement & Podium.rvt'),
'AR-MOD-XX-XX-006': os.path.join(projfilesfolder,'AR-MOD-XX-XX-006-RVT - Interior Tower.rvt'),
'AR-MOD-XX-XX-009': os.path.join(projfilesfolder,'AR-MOD-XX-XX-009-RVT - MEP Place Holders.rvt'),
'AR-MOD-XX-XX-010': os.path.join(projfilesfolder,'AR-MOD-XX-XX-010-RVT - Master Grid.rvt'),
'AR-MOD-XX-XX-015': os.path.join(sitefilesfolder,'AR-MOD-XX-XX-015-RVT - Clearance Zones.rvt'),
'AR-MOD-XX-XX-020': os.path.join(sitefilesfolder,'AR-MOD-XX-XX-020-RVT - DCP Massing.rvt'),
'AR-MOD-XX-XX-025': os.path.join(sitefilesfolder,'AR-MOD-XX-XX-025-RVT - 33 Alfred St.rvt'),
'AR-MOD-XX-XX-800': os.path.join(sitefilesfolder,'AR-MOD-XX-XX-800-RVT - MPX Site.rvt'),
'AR-MOD-XX-XX-900': os.path.join(sitefilesfolder,'AR-MOD-XX-XX-900-RVT - Enscape 3D.rvt'),
'AR-MOD-XX-XX-999': os.path.join(areafilesfolder,'AR-MOD-XX-XX-999-RVT - Area Analysis Model.rvt')
}

ACONEXProjFiles = {
#ASPECT
'LA-MOD-XX-XX-001': r'X:\003 - Multiplex\Design\BIM\_Revit\8.0 Revit Links\1.0 MPX\ASPECT\LA-MOD-XX-XX-001-RVT-17 - Landscape.rvt', # Up to date for XMAS
#AXIS
'AXS-HY-MOD-XX-001': r'X:\003 - Multiplex\Design\BIM\_Revit\8.0 Revit Links\1.0 MPX\AXIS\AXS-HY-MOD-XX-001-RVT-27 - Hydraulic Services.rvt', # Up to date for XMAS
#BG&E
'ST-MOD-XX-XX-001': r'X:\003 - Multiplex\Design\BIM\_Revit\8.0 Revit Links\1.0 MPX\BG&E\001 - ST-MOD-XX-XX-001-RVT - PODIUM\ST-MOD-XX-XX-001-RVT-69 - PODIUM.rvt', # Up to date for XMAS
'ST-MOD-XX-XX-002': r'X:\003 - Multiplex\Design\BIM\_Revit\8.0 Revit Links\1.0 MPX\BG&E\002 - ST-MOD-XX-XX-002-RVT - TOWER\ST-MOD-XX-XX-002-RVT-72 - TOWER.rvt', # Up to date for XMAS
'ST-MOD-XX-XX-003': r'X:\003 - Multiplex\Design\BIM\_Revit\8.0 Revit Links\1.0 MPX\BG&E\003 - ST-MOD-XX-XX-003-RVT - EXISTING\ST-MOD-XX-XX-003-RVT-63 - EXISTING.rvt', # Up to date for XMAS
'ST-MOD-XX-XX-004': r'X:\003 - Multiplex\Design\BIM\_Revit\8.0 Revit Links\1.0 MPX\BG&E\004 - ST-MOD-XX-XX-004-RVT - 33A ALFRED\ST-MOD-XX-XX-004-RVT-31 - 33A ALFRED.rvt', # Up to date for XMAS
'ST-MOD-XX-XX-005': r'X:\003 - Multiplex\Design\BIM\_Revit\8.0 Revit Links\1.0 MPX\BG&E\005 - ST-MOD-XX-XX-005-RVT - INFILL\ST-MOD-XX-XX-005-RVT-17 - INFILL.rvt', # Up to date for XMAS
'ST-MOD-XX-XX-007': r'X:\003 - Multiplex\Design\BIM\_Revit\8.0 Revit Links\1.0 MPX\BG&E\007 - ST-MOD-XX-XX-007-RVT - CROWN\ST-MOD-XX-XX-007-RVT-09 - CROWN.rvt', # Up to date for XMAS
#ECJV
'ECJ-ME-MOD-XX-001': r'X:\003 - Multiplex\Design\BIM\_Revit\8.0 Revit Links\1.0 MPX\ECJV\ECJ-ME-MOD-XX-001-RVT-31 - Mechanical Services.rvt', # Up to date for XMAS
#MPX
'MPX-PM-MOD-XX-001': r'X:\003 - Multiplex\Design\BIM\_Revit\8.0 Revit Links\1.0 MPX\MPX\MPX-PM-MOD-XX-001-RVT-02 - Crane Place Holders.rvt', # Up to date for XMAS
#PFPS
'PFS-FS-MOD-XX-001': r'X:\003 - Multiplex\Design\BIM\_Revit\8.0 Revit Links\1.0 MPX\PFPS\001 - PFS-FS-MOD-XX-001\PFS-FS-MOD-XX-001-RVT-30 - Sprinkler Layout.rvt', # Up to date for XMAS
'PFS-FS-MOD-XX-002': r'X:\003 - Multiplex\Design\BIM\_Revit\8.0 Revit Links\1.0 MPX\PFPS\002 - PFS-FS-MOD-XX-002\PFS-FS-MOD-XX-002-RVT-30 - Fire Hydrant Layout.rvt', # Up to date for XMAS
'PFS-FD-MOD-XX-003': r'X:\003 - Multiplex\Design\BIM\_Revit\8.0 Revit Links\1.0 MPX\PFPS\003 - PFS-FD-MOD-XX-003\PFS-FD-MOD-XX-003-RVT-30 - Fire Detection & EWIS.rvt', # Up to date for XMAS
'PFS-FS-MOD-XX-004': r'X:\003 - Multiplex\Design\BIM\_Revit\8.0 Revit Links\1.0 MPX\PFPS\004 - PFS-FS-MOD-XX-004\PFS-FS-MOD-XX-004-RVT-02 - Temporary Fire.rvt', # Up to date for XMAS
#STAR
'STA-EL-MOD-XX-001': r'X:\003 - Multiplex\Design\BIM\_Revit\8.0 Revit Links\1.0 MPX\STAR\STA-EL-MOD-XX-001-RVT-29 - ELECTRICAL SERVICES.rvt', # Up to date for XMAS
#WEBB
'ASP3-MOD-XX-XX-001': r'X:\003 - Multiplex\Design\BIM\_Revit\8.0 Revit Links\1.0 MPX\WEBB\ASP3-MOD-XX-XX-001-RVT-28 - 50 BRIDGE SUBSTATION MODEL.rvt', # Up to date for XMAS
#DRS
'ID-MOD-XX-XX-001': r'X:\003 - Multiplex\Design\BIM\_Revit\8.0 Revit Links\2.0 AMPC\DRS\ID-MOD-XX-XX-001-RVT-05-SD_Lobby and Terrace.rvt', # Up to date for XMAS
'ID-MOD-XX-XX-002': r'X:\003 - Multiplex\Design\BIM\_Revit\8.0 Revit Links\2.0 AMPC\DRS\ID-MOD-XX-XX-002-RVT-01-SD_The Club lvl 02-03 (2017-03-21).rvt' # Up to date for XMAS
}

otherProjLinks = {
#BVN
'Site Context.rvt': r'X:\003 - Multiplex\Design\BIM\_Revit\8.0 Revit Links\1.0 MPX\BVN\Site Context\Site Context.rvt',
'33 Alfred Interface.rvt': r'X:\003 - Multiplex\Design\BIM\_Revit\4.0 CAD Links\1.0 MPX\BVN\33 Alfred Interface.rvt',
#AAM
'SU-MOD-XX-XX-001 - AAM Survey.rvt': r'X:\003 - Multiplex\Design\BIM\_Revit\4.0 CAD Links\1.0 MPX\AAM\SU-MOD-XX-XX-001 - AAM Survey.rvt',
#AvroKO
'AvroKO - CAD Links.rvt': r'X:\003 - Multiplex\Design\BIM\_Revit\4.0 CAD Links\2.0 AMPC\AvroKO\AvroKO - CAD Links.rvt',
#WEBB
'WEBB Substations CAD.rvt': r'X:\003 - Multiplex\Design\BIM\_Revit\4.0 CAD Links\1.0 MPX\WEBB\ASP3-MOD-XX-XX-001-RVT-28 - 50 BRIDGE SUBSTATION MODEL.rvt',
#Van der Meer
'SSE-ST-MOD - Levels B05 - L02.rvt': r'X:\003 - Multiplex\Design\BIM\_Revit\8.0 Revit Links\1.0 MPX\VANDERMEER\001 - Levels B5 - 02\SSE-ST-MOD - Levels B05 - L02.rvt', # Up to date for XMAS
'SSE-ST-MOD - Levels L02 - L06.rvt': r'X:\003 - Multiplex\Design\BIM\_Revit\8.0 Revit Links\1.0 MPX\VANDERMEER\002 - Levels 02 - 06\SSE-ST-MOD - Levels L02 - L06.rvt', # Up to date for XMAS
'SSE-ST-MOD - Levels L07 - L14.rvt': r'X:\003 - Multiplex\Design\BIM\_Revit\8.0 Revit Links\1.0 MPX\VANDERMEER\003 - Levels 07 - 14\SSE-ST-MOD - Levels L07 - L14.rvt', # Up to date for XMAS
'SSE-ST-MOD - Levels L15 - L20.rvt': r'X:\003 - Multiplex\Design\BIM\_Revit\8.0 Revit Links\1.0 MPX\VANDERMEER\004 - Levels 15 - 20\SSE-ST-MOD - Levels L15 - L20.rvt', # Up to date for XMAS
'SSE-ST-MOD - Levels L21 - L27.rvt': r'X:\003 - Multiplex\Design\BIM\_Revit\8.0 Revit Links\1.0 MPX\VANDERMEER\004 - Levels 21 - 27\SSE-ST-MOD - Levels L21 - L27.rvt', # Up to date for XMAS
#LTS
'LTS Survey Plans.rvt': r'X:\003 - Multiplex\Design\BIM\_Revit\4.0 CAD Links\1.0 MPX\LTS\LTS Survey Plans\LTS Survey Plans.rvt',
'LTS Survey South Stairs.rvt': r'X:\003 - Multiplex\Design\BIM\_Revit\4.0 CAD Links\1.0 MPX\LTS\LTS South Stair\LTS Survey South Stairs.rvt',
'LTS SOUTH STAIR SURVEY.rvt': r'X:\003 - Multiplex\Design\BIM\_Revit\4.0 CAD Links\1.0 MPX\LTS\LTS South Stair\LTS Survey South Stairs.rvt',
#DRS CAD
'DRS - CAD Links.rvt': r'X:\003 - Multiplex\Design\BIM\_Revit\4.0 CAD Links\2.0 AMPC\DRS\DRS - CAD Links.rvt',
#ASPECT
'ASPECT Site Background.rvt': r'X:\003 - Multiplex\Design\BIM\_Revit\4.0 CAD Links\1.0 MPX\ASPECT\Site Background\ASPECT Site Background.rvt'
}
#'': r'',

#------------------------------------------------------------------------#
def GetLinkName(aLink):
  #return [x.strip() for x in Element.Name.GetValue(aLink).split(':')]
  return Element.Name.GetValue(aLink)
#------------------------------------------------------------------------#
def LinkAlreadyPathed(aLink, thePath):
  result = False
  #Grab the Model Path of the Link
  er = aLink.GetExternalFileReference()
  mp = er.GetPath()
  #Convert it so we can read it
  path = ModelPathUtils.ConvertModelPathToUserVisiblePath(mp)
  #This will be a UNC path so convert it to the X: drive path
  xpath = os.path.splitunc(path)[1].replace('\\13\\s1309002.yel','X:')
  #Check if they point to the same file 
  if xpath == thePath:
    result = True
    
  return result
  
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
def RePathBVNModel(aLink):
  global BVNProjfiles
  
  linkName = GetLinkName(aLink)
  #Grab the first 16 (0-15) characters of the filename
  keyval = linkName[:16]
   
  #Get the New Path from the Dictionary above
  if keyval in BVNProjfiles.Keys:
    newPath = BVNProjfiles[keyval]
    return RePathLinks(aLink, newPath)
  else:
    print 'Key Not Found: ' + keyval
    return False
#------------------------------------------------------------------------# 
def GetLatestRevisionFromFolder(fileID, folderpath):
  
  # list of Revit files in the folder that match
  # both the start of the filename and end with .rvt
  filenames = [fn for fn in os.listdir(folderpath)
               if fn.startswith(fileID)]
 
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
     
#------------------------------------------------------------------------#
def RePathConsSubModel(aLink):
  global ACONEXProjFiles
  
  linkName = GetLinkName(aLink)
  #Grab the first 16/17 characters of the filename up to but not
  #including the "-RVT"
  keyval = linkName[:linkName.find('-RVT')]

  try:
    #Get the New Path from the Dictionary above
    newPath = ACONEXProjFiles[keyval]
    #Find the latest Revision in the new folder <-------------<<< To Do
    #
    #print 'newPath: ' + newPath
    #latest = GetLatestRevisionFromFolder(fileID, newPath)
    #print '+-------+' + latest
    #Rebuild the path
    #newlink = '\\'.join(latest)
    
    if newPath:
      return RePathLinks(aLink, newPath)
  except Exception as e:
    print 'Unable to Re-Path: ' + linkName
    return False
  
#------------------------------------------------------------------------#
def RePathGeneralModel(aLink):
  global otherProjLinks
  
  linkName = GetLinkName(aLink)
  #In this case use the whole filename as the dict Key 
  try:
    newPath = otherProjLinks[linkName]
    if newPath:
      return RePathLinks(aLink, newPath)
  except Exception as e:
    print 'Unable to Re-Path: ' + linkName
    return False

#------------------------------------------------------------------------# 
def RePathLinks(aLink, newPath):
  # Check to make sure that the file needs repathing first
  if LinkAlreadyPathed(aLink, newPath):
    print 'ALREADY CURRENT: ' + GetLinkName(aLink)
  else:
    modelpath = ModelPathUtils.ConvertUserVisiblePathToModelPath(newPath)
    try:
      # Re-Path the file
      reloadResults = aLink.LoadFrom(modelpath, WorksetConfiguration())
      return True
    except Exception as e:
      print 'Error Repathing ' + GetLinkName(aLink)
      print newPath
      print e.message
      print '-' * 75
      return False
  
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
    thePath = os.path.dirname(os.path.abspath(ModelPathUtils.ConvertModelPathToUserVisiblePath(mp)))
    
  return thePath
#------------------------------------------------------------------------#  
def main():
  
  #Get a List of the LinkType Elements in the model
  theLinks = GetAllLinks()
  
  for aLink in theLinks:
    linkName = GetLinkName(aLink)
    # If We Have a BVN Project File with No Revision Number
    if '-RVT - ' in linkName:
      #print linkName + ' is a BVN Local Model'
      if RePathBVNModel(aLink):
        print 'UPDATED: ' + linkName 
      else:
        print 'Error updating: ' + linkName
        
    else:
      # If We have a consultant or Subcontractor model with a revision Number
      if '-RVT-' in linkName:
        #print linkName + ' is a Consultant or Subcontractor Model'
        if RePathConsSubModel(aLink):
          print 'UPDATED: ' + linkName
        else:  
          print 'Error updating: ' + linkName
      else:
        #We must have a non revision Controlled General Link File
        #print linkName + ' is a General Link with No Revision'
        if RePathGeneralModel(aLink):
          print 'UPDATED: ' + linkName
        else:  
          print 'Error updating: ' + linkName
          
  print '         +------------------------------------+'
  print '         |  >>--->  C O M P L E T E  <---<<   |'  
  print '         +------------------------------------+'
  
#------------------------------------------------------------------------# 
if __name__ == '__main__': main()

