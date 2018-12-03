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
areafilesfolder = r'X:\003 - Multiplex\Design\BIM\_Revit\1.0 Project Files\3.0 Details\Areas'

BVNProjfiles = {
'AR-MOD-XX-XX-001': os.path.join(sitefilesfolder,'AR-MOD-XX-XX-001-RVT - Site.rvt'),
'AR-MOD-XX-XX-002': os.path.join(projfilesfolder,'AR-MOD-XX-XX-002-RVT - Structure.rvt'),
'AR-MOD-XX-XX-003': os.path.join(projfilesfolder,'AR-MOD-XX-XX-003-RVT - Crown Louvers.rvt'),
'AR-MOD-XX-XX-004': os.path.join(projfilesfolder,'AR-MOD-XX-XX-004-RVT - Facade Tower.rvt'),
'AR-MOD-XX-XX-005': os.path.join(projfilesfolder,'AR-MOD-XX-XX-005-RVT - Basement & Poium.rvt'),
'AR-MOD-XX-XX-006': os.path.join(projfilesfolder,'AR-MOD-XX-XX-006-RVT - Interior Tower.rvt'),
'AR-MOD-XX-XX-009': os.path.join(projfilesfolder,'AR-MOD-XX-XX-009-RVT - MEP Place Holders.rvt'),
'AR-MOD-XX-XX-010': os.path.join(projfilesfolder,'AR-MOD-XX-XX-010-RVT - Master Grid.rvt'),
'AR-MOD-XX-XX-015': os.path.join(sitefilesfolder,'AR-MOD-XX-XX-015-RVT - Clearance Zones.rvt'),
'AR-MOD-XX-XX-020': os.path.join(sitefilesfolder,'AR-MOD-XX-XX-020-RVT - DCP Massing.rvt'),
'AR-MOD-XX-XX-800': os.path.join(sitefilesfolder,'AR-MOD-XX-XX-800-RVT - MPX Site.rvt'),
'AR-MOD-XX-XX-900': os.path.join(sitefilesfolder,'AR-MOD-XX-XX-900-RVT - Enscape 3D.rvt'),
'AR-MOD-XX-XX-999': os.path.join(areafilesfolder,'AR-MOD-XX-XX-999-RVT - Area Analysis Model.rvt')
}

ACONEXProjFiles = {
#ASPECT
'LA-MOD_XX_XX_001': r'X:\003 - Multiplex\Design\BIM\_Revit\8.0 Revit Links\1.0 MPX\ASPECT',
#AXIS
'AXS-HY-MOD-XX-001': r'X:\003 - Multiplex\Design\BIM\_Revit\8.0 Revit Links\1.0 MPX\AXIS',
#BG&E
'ST-MOD-XX-XX-001': r'X:\003 - Multiplex\Design\BIM\_Revit\8.0 Revit Links\1.0 MPX\BG&E\001 - ST-MOD-XX-XX-001-RVT - PODIUM',
'ST-MOD-XX-XX-002': r'X:\003 - Multiplex\Design\BIM\_Revit\8.0 Revit Links\1.0 MPX\BG&E\002 - ST-MOD-XX-XX-002-RVT - TOWER',
'ST-MOD-XX-XX-003': r'X:\003 - Multiplex\Design\BIM\_Revit\8.0 Revit Links\1.0 MPX\BG&E\003 - ST-MOD-XX-XX-003-RVT - EXISTING',
'ST-MOD-XX-XX-004': r'X:\003 - Multiplex\Design\BIM\_Revit\8.0 Revit Links\1.0 MPX\BG&E\004 - ST-MOD-XX-XX-004-RVT - 33A ALFRED',
'ST-MOD-XX-XX-005': r'X:\003 - Multiplex\Design\BIM\_Revit\8.0 Revit Links\1.0 MPX\BG&E\005 - ST-MOD-XX-XX-005-RVT - INFILL',
'ST-MOD-XX-XX-007': r'X:\003 - Multiplex\Design\BIM\_Revit\8.0 Revit Links\1.0 MPX\BG&E\007 - ST-MOD-XX-XX-007-RVT - CROWN',
#ECJV
'ECJ-ME-MOD-XX-001': r'X:\003 - Multiplex\Design\BIM\_Revit\8.0 Revit Links\1.0 MPX\ECJV',
#MPX
'MPX-PM-MOD-XX-001': r'X:\003 - Multiplex\Design\BIM\_Revit\8.0 Revit Links\1.0 MPX\MPX',
#PFPS
'PFS-FS-MOD-XX-001': r'X:\003 - Multiplex\Design\BIM\_Revit\8.0 Revit Links\1.0 MPX\PFPS',
'PFS-FS-MOD-XX-002': r'X:\003 - Multiplex\Design\BIM\_Revit\8.0 Revit Links\1.0 MPX\PFPS',
'PFS-FD-MOD-XX-003': r'X:\003 - Multiplex\Design\BIM\_Revit\8.0 Revit Links\1.0 MPX\PFPS',
'PFS-FS-MOD-XX-004': r'X:\003 - Multiplex\Design\BIM\_Revit\8.0 Revit Links\1.0 MPX\PFPS',
#STAR
'STA-EL-MOD-XX-001': r'X:\003 - Multiplex\Design\BIM\_Revit\8.0 Revit Links\1.0 MPX\STAR',
#WEBB
'ASP3-MOD-XX-XX-001': r'X:\003 - Multiplex\Design\BIM\_Revit\8.0 Revit Links\1.0 MPX\WEBB'
}

otherProjLinks = {
'Site Context.rvt': r'X:\003 - Multiplex\Design\BIM\_Revit\8.0 Revit Links\1.0 MPX\BVN\Site Context',
'33 Alfred Interface.rvt': r'X:\003 - Multiplex\Design\BIM\_Revit\4.0 CAD Links\1.0 MPX\BVN',
'SU-MOD-XX-XX-001 - AAM Survey.rvt': r'X:\003 - Multiplex\Design\BIM\_Revit\4.0 CAD Links\1.0 MPX\AAM',
'AvroKO - CAD Links.rvt': r'X:\003 - Multiplex\Design\BIM\_Revit\4.0 CAD Links\2.0 AMPC\AvroKO',
'WEBB Substations CAD.rvt': r'X:\003 - Multiplex\Design\BIM\_Revit\4.0 CAD Links\1.0 MPX\WEBB',
'SE-ST-MOD - Levels B05 - L02.rvt': r'X:\003 - Multiplex\Design\BIM\_Revit\8.0 Revit Links\1.0 MPX\VANDEMEER',
'SE-ST-MOD - Levels L02 - L06.rvt': r'X:\003 - Multiplex\Design\BIM\_Revit\8.0 Revit Links\1.0 MPX\VANDEMEER',
'SE-ST-MOD - Levels L07 - L14.rvt': r'X:\003 - Multiplex\Design\BIM\_Revit\8.0 Revit Links\1.0 MPX\VANDEMEER',
'SE-ST-MOD - Levels L15 - L20.rvt': r'X:\003 - Multiplex\Design\BIM\_Revit\8.0 Revit Links\1.0 MPX\VANDEMEER',
}



#'': r'',

# Is this link a BVN Project Link
# Look in BVNProjFiles dict using the full filename (No revision required)
# if '-RVT - ' in LinkName:
#   pass


# Is this link an Aconex Shared Project Link
# Look in the ACONEXProjFiles dict and do a lookup for latest revision
# if '-RVT-' in LinkName
#   pass

# If not then look in the last dict using full filename as key
# No revision
#------------------------------------------------------------------------#
def GetLinkName(aLink):
  #return [x.strip() for x in Element.Name.GetValue(aLink).split(':')]
  return Element.Name.GetValue(aLink)
#------------------------------------------------------------------------#
def GetAllLinks():
  theLinks = (
    FilteredElementCollector(doc)
    .OfCategory(BuiltInCategory.OST_RvtLinks)
    #Only Link Types, NOT Link Instances
    .Where(lambda link: RevitLinkType == type(link))
    )
    
  return theLinks.ToList()
#------------------------------------------------------------------------#
def RePathBVNModel(aLink):
  global BVNProjfiles

  linkName = GetLinkName(aLink)
  #Grab the first 16 (0-15) characters of the filename
  keyvale = linkName[:-15]
  #Get the New Path from the Dictionary above
  newPath = BVNProjfiles[keyval]
  if newPath:
    return rePathLinks(aLink, newPath)
  else:
    return False
  
#------------------------------------------------------------------------#
def RePathConsSubModel(aLink):
  global ACONEXProjFiles
  
  linkName = GetLinkName(aLink)
  #Grab the first 16 (0-15) characters of the filename
  keyvale = linkName[:-15]
  #Get the New Path from the Dictionary above
  newPath = ACONEXProjFiles[keyval]
  #Find the latest Revision in the new folder <-------------<<< To Do
  #
  #
  #
  if newPath:
    return rePathLinks(aLink, newPath)
  else:
    return False

#------------------------------------------------------------------------#
def RePathGeneralModel(aLink):
  global otherProjLinks
  
  linkName = GetLinkName(aLink)
  #In this case use the whole filename as the dict Key 
  newPath = otherProjLinks[linkName]
  if newPath:
    return rePathLinks(aLink, newPath)
  else:
    return False

#------------------------------------------------------------------------# 
def RePathLinks(aLink, newPath):
  newLink = ModelPathUtils.ConvertUserVisiblePathToModelPath(newPath)
  try:
    reloadResults = aLink.LoadFrom(modelpath, WorksetConfiguration())
    return True
  except Exception as e:
    print 'Error Repathing ' + GetLinkName(aLink)
    print newPath
    print e.message
    print '-' * 75
    return False
#------------------------------------------------------------------------#
  
def main():
  
  #Get a List of the LinkType Elements in the model
  theLinks = GetAllLinks()
  
  for aLink in theLinks:
    linkName = GetLinkName(aLink)
    # If We Have a BVN Project File with No Revision Number
    if '-RVT - ' in linkName:
      print linkName + ' is a BVN Local Model'
      RePathBVNModel(aLink)
    else:
      # If We have a consultant or Subcontractor model with a revision Number
      if '-RVT-' in linkName:
        print linkName + ' is a Consultant or Subcontractor Model'
        RePathConsSubModel(aLink)
      else:
        #We must have a non revision Controlled General Link File
        print linkName + ' is a General Link with No Revision'
        RePathGeneralModel(aLink)
     
  
#------------------------------------------------------------------------# 
if __name__ == '__main__': main()
