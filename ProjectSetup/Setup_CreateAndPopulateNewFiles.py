#========================================================================#
#      _____               __                            
#      \_   \__ _ _ __     \ \  __ _ _ __ ___   ___  ___ 
#       / /\/ _` | '_ \     \ \/ _` | '_ ` _ \ / _ \/ __|
#    /\/ /_| (_| | | | | /\_/ / (_| | | | | | |  __/\__ \
#    \____/ \__,_|_| |_| \___/ \__,_|_| |_| |_|\___||___/
#
#
#  The Script automates the creation of a typical Building and site
#  model for a new Project Setup, complete with all meta data
#
#  March 2021
#
#================ EDIT THESE VALUES BEFORE RUNNING ======================#
BVN_Project_Number =        '2103015'
BVN_projectAbbr =           'ANX'
BVN_Project_Name =          'The Annex BVN Studio'
BVN_Client =                'BVN'
BVN_Client_ProjectNumber =  '2103015'
BVN_Project_Type =          'Commercial'
BVN_Building_Name =         '12 Creek Street'
BVN_MM_Model_Name_BLDG =    'The Annex Building'
BVN_MM_Model_Name_SITE =    'The Annex Site'
#========================================================================#
import os
import datetime

#Convert all of the parameter variables to uppercase.
BVN_Project_Number = BVN_Project_Number.upper()
BVN_projectAbbr = BVN_projectAbbr.upper()
BVN_Project_Name = BVN_Project_Name.upper()
BVN_Client = BVN_Client.upper()
BVN_Client_ProjectNumber = BVN_Client_ProjectNumber.upper()
BVN_Project_Type = BVN_Project_Type.upper()
BVN_Building_Name = BVN_Building_Name.upper()
BVN_MM_Model_Name_BLDG = BVN_MM_Model_Name_BLDG.upper()
BVN_MM_Model_Name_SITE = BVN_MM_Model_Name_SITE.upper()
#-------------------------------------------------------
def getYearFromProjectId(projectId):
  return projectId [:2]
#-------------------------------------------------------
def getMonthFromProjectId(projectId):
  return projectId [2:4]
#-------------------------------------------------------
def getBVNTemplate():
    version = uiapp.Application.VersionNumber
    templatepath = '//dc2-file001/practice/InfoTech/BIM/Revit/RevitStandards' + version + '/01_Template/BVN.rte'
    return templatepath
#-------------------------------------------------------
def ValidateProjectID(projectID):
  result = True
  # Make sure that Project ID is numerical
  if not projectID.isnumeric(): 
    return False
  # Make sure that Project ID is 7 digits
  if not len(projectID) == 7:
    return False
  # Make sure that the year is valid, ie this year or less.
  # Hard coding dates to second millenium 2000
  theYear = (int(getYearFromProjectId(projectID)) + 2000)
  currYear = datetime.datetime.now().year
  if not theYear <= currYear:
    return False
  # Make sure that the second two digits are between
  # 01 and 12 (January to December)
  theMonth = int(getMonthFromProjectId(projectID))
  if not (theMonth > 0 and theMonth <=12):
    return False
  # If All of the above pass then return True!!
  return True
#-------------------------------------------------------
def ShowDone():
  print('\n')
  print('  ____   ___  _   _ _____       _ ')
  print(' |  _ \ / _ \| \ | | ____|     | |')
  print(' | | | | | | |  \| |  _|       | |')
  print(' | |_| | |_| | |\  | |___ _ _ _|_|')
  print(' |____/ \___/|_| \_|_____(_|_|_|_)')
  print('\n')
#-------------------------------------------------------
def getNewfileName(BVN_Project_Number, BVN_projectAbbr, fname):
  # Get the Year that the Project Belongs to
  theYear = getYearFromProjectId(BVN_Project_Number)
  
  #Build the Proposed Path
  theName = 'p:/'
  theName = theName + theYear
  theName = theName + '/'
  theName = theName + BVN_Project_Number
  theName = theName + '.000/Design/BIM/_Revit/1.0 Project Files/AR_'
  theName = theName + BVN_Project_Number
  theName = theName + '_'
  theName = theName + BVN_projectAbbr
  theName = theName + '_'
  theName = theName + fname
  theName = theName + '.rvt'
  
  return theName
#=================GLOBAL & PROJECT PARAMETERS============================#
def setGlobalParameter(doc, pname, pvalue):
  gpid = GlobalParametersManager.FindByName(doc,pname)
  theValue = StringParameterValue(pvalue)
  if GlobalParametersManager.IsValidGlobalParameter(doc, gpid):
    gp = doc.GetElement(gpid)
    tranny = Transaction(doc)
    try:
      tranny.Start('Updating GP:' + pname)
      gp.SetValue(theValue)
      tranny.Commit()
      tranny.Dispose()
    except Exception as e:
      print 'Error setting Global Parameter ' + pname
      print e.message
      tranny.RollBack()
      tranny.Dispose()
  else:
    print 'Error in setGlobalParameter'
    print 'cannot find Global Parameter called: ' + pname
#-------------------------------------------------------
def setProjectParameter(doc, pname, pvalue):
  pInfo = doc.ProjectInformation
  param = pInfo.LookupParameter(pname)
  if Parameter == type(param):
    tranny = Transaction(doc)
    try:
      tranny.Start('Updating Info:' + pname)
      param.Set(pvalue)
      tranny.Commit()
      tranny.Dispose()
    except Exception as e:
      print 'Error setting Project Parameter ' + pname
      print e.message
      tranny.RollBack()
      tranny.Dispose()
  else:
    print "Couldn't find parameter: " + pname
#-------------------------------------------------------
def setParams(doc, modelName):
  #Set Global Parameters
  setGlobalParameter(doc, "BVN_Project Name", BVN_Project_Name)
  setGlobalParameter(doc, "BVN_Project Number", BVN_Project_Number)
  setGlobalParameter(doc, "BVN_Client", BVN_Client)
  if 'SITE' in modelName:
    setGlobalParameter(doc, "BVN_MM_Model Name", BVN_MM_Model_Name_SITE)
  else:
    setGlobalParameter(doc, "BVN_MM_Model Name", BVN_MM_Model_Name_BLDG)
  
  #Set Project Parameters
  setProjectParameter(doc, "Client Name", BVN_Client)
  setProjectParameter(doc, "Project Name",BVN_Project_Name)
  setProjectParameter(doc, "Project Number",BVN_Project_Number)
  setProjectParameter(doc, "Building Name",BVN_Building_Name)
  setProjectParameter(doc, "Original Model By","BVN")
  setProjectParameter(doc, "Project Type", BVN_Project_Type)
  setProjectParameter(doc, "Client Project Number",BVN_Client_ProjectNumber) 
#=================WORKSHARING AND WORKSETS============================#
def getWorksetsBuilding():
  #The default worksets for a Building Model
  newWorksets = [
    '99_LEVELS AND GRIDS',
    '30_INTERIOR',
    '00_FACADE',
    '10_STRUCTURE',
    '20_VERTICAL CIRCULATION',
    '40_FF&E',
    '51_ENTOURAGE',
    '60_MASSING',
    '70_SAFETY IN DESIGN',
    '90_LINK_BVN_SITE',
    '92_LINK_CAD_SURVEY'
    ]
    
  return newWorksets
#-------------------------------------------------------
def getWorksetsSite():
  #The default worksets for a Site Model
  newWorksets = [
    '99_LEVELS AND GRIDS',
    '50_SITE',
    '50_SITE BOUNDARY',
    '51_ENTOURAGE',
    '60_MASSING',
    '70_SAFETY IN DESIGN',
    '90_LINK_BVN_BUILDING',
    '92_LINK_CAD_SURVEY'
    ]
    
  return newWorksets
#-------------------------------------------------------

#-------------------------------------------------------
def makeWorkshared(newModel, modelName):
  
  # Grab the appropriate worksets
  # if this is a SITE model
  if 'SITE' in modelName.upper():
    theWorksets = getWorksetsSite()
  # Else if it is a BUILDING model
  else:
    theWorksets = getWorksetsBuilding()
  
  # Enable Worksharing and create the default Worksets
  newModel.EnableWorksharing(theWorksets[0],theWorksets[1])
  
  #Get the Workset Table
  wst = newModel.GetWorksetTable()
  
  # Make sure that each of the newWorksets are unique
  # and create them
  for aWorkset in theWorksets:         # <---<< Modify this to skip first two worksets...!!!
    #Make sure that the work doesn't already exist
    if wst.IsWorksetNameUnique(newModel,aWorkset):
      try:
        tranny = Transaction(newModel)
        tranny.Start('Creating Workset ' + aWorkset)
        #Create the Workset
        Workset.Create(newModel,aWorkset)
        tranny.Commit()
      except Exception  as e:
        print e.message
        tranny.RollBack()
        tranny.Dispose()
    else:
      print aWorkset + ' Already Exists'
#-------------------------------------------------------
def createBVNModel(modelName, templateBVN):
  # Create a new model from the chosen template
  newModel = uiapp.Application.NewProjectDocument(templateBVN)
  
  # Set the Project and Global Parameters
  setParams(newModel, modelName)
  
  # Create Worksets and make worksharing
  makeWorkshared(newModel, modelName)
  
  # Make the Worksharing Options
  WSAO = WorksharingSaveAsOptions()
  WSAO.SaveAsCentral = True
  options = SaveAsOptions()
  options.SetWorksharingOptions(WSAO)
  
  # Save the Model and Close it
  newModel.SaveAs(modelName, options)
  
  # Synch and Relinquish Worksets
  relinqOptions = RelinquishOptions(True)
  relinqOptions.UserWorksets = True
  
  #Synch Settings including message and Compact the File.
  synch = SynchronizeWithCentralOptions()
  synch.Comment = 'BVN Central Model Created at ' + datetime.datetime.now().isoformat()
  synch.Compact = True
  synch.SaveLocalBefore = False
  synch.SetRelinquishOptions(relinqOptions)
  
  transact = TransactWithCentralOptions()
  
  newModel.SynchronizeWithCentral(transact, synch)

  newModel.Close(True)
#-------------------------------------------------------
app = uiapp.Application

OKtoGO = True

newFileBLDG = getNewfileName(BVN_Project_Number, BVN_projectAbbr, 'BUILDING')
newFileSITE = getNewfileName(BVN_Project_Number, BVN_projectAbbr, 'SITE')
templateBVN = getBVNTemplate()

# Make sure that the path to the template is valid
if os.path.exists(templateBVN):
  print templateBVN
else:
  OKtoGO = False
  print 'Template Not Found'

# Make sure that the project number is valid and meets certain check criteria
if ValidateProjectID(BVN_Project_Number):
  print newFileBLDG
  print newFileSITE
  
else:
  OKtoGO = False
  print "That Project Number doesn't seem to be valid...!!!"

# Make sure that the new files don't already exist
if os.path.exists(newFileBLDG):
  OKtoGO = False
  print 'File Already Exists:\n' + newFileBLDG
  

if os.path.exists(newFileSITE):
  OKtoGO = False
  print 'File Already Exists:\n' + newFileSITE


if OKtoGO:
  #Create the new Models
  createBVNModel(newFileBLDG, templateBVN)
  createBVNModel(newFileSITE, templateBVN)
  ShowDone()
  

  


