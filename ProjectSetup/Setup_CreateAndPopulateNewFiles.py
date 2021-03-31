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
BVN_Project_Number =        '1901001'
BVN_projectAbbr =           'BVN'
BVN_Project_Name =          'Project Name'
BVN_Client =                'BVN'
BVN_Client_ProjectNumber =  '1901001'
BVN_Project_Type =          'Test'
BVN_Building_Name =         'Test File Setup'
BVN_MM_Model_Name_BLDG =    'Test CAD Link File'
BVN_MM_Model_Name_SITE =    'Test CAD Link Site'
BVN_LatLong = 53.5614228062953, -2.1142019557370655
#========================================================================#
import os
import datetime
import math

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

#Get Lat and Lon 
lat = BVN_LatLong[0]
lon = BVN_LatLong[1]

#Convert Lat & Lon to radians for use in Revit.
BVN_Lat = lat / (180/math.pi)
BVN_Lon = lon / (180/math.pi)
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
def isValidSurveyFolder(folder):
  return (os.path.exists(folder) and os.path.isdir(folder))
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
#-------------------------------------------------------
def getCADLINKfileName(BVN_Project_Number, BVN_projectAbbr, fname):
  # Get the Year that the Project Belongs to
  theYear = getYearFromProjectId(BVN_Project_Number)
  
  #Build the Proposed Path
  theName = 'p:/'
  theName = theName + theYear
  theName = theName + '/'
  theName = theName + BVN_Project_Number
  theName = theName + '.000/Design/BIM/_Revit/4.0 CAD Links/AR_CADLINK_'
  theName = theName + BVN_Project_Number
  theName = theName + '_'
  theName = theName + BVN_projectAbbr
  theName = theName + '_'
  theName = theName + fname
  theName = theName + '.rvt'
  
  return theName
#-------------------------------------------------------
def getCADLinkSurveyFolder(BVN_Project_Number):
  # Get the Year that the Project Belongs to
  theYear = getYearFromProjectId(BVN_Project_Number)
  
  #Build the Proposed Path
  theName = 'p:/'
  theName = theName + theYear
  theName = theName + '/'
  theName = theName + BVN_Project_Number
  theName = theName + '.000/Design/BIM/_Revit/4.0 CAD Links/SURVEY'
  
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
#-------------------------------------------------------
def setBasicParams(doc, modelName):
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
#-------------------------------------------------------
def AddBasicParameters(doc):
  #Basic Parameters to be created in Non BVN Template Models
  ParamNames = [
    'BVN_Client',
    'BVN_Project Number',
    'BVN_Project Name',
    'BVN_MM_Model Name'
  ]

  for aParam in ParamNames:
    if GlobalParametersManager.IsUniqueName(doc,aParam):
      try:
        tranny = Transaction(doc)
        tranny.Start('Creating Global Parameter: ' + aParam)
        
        # Create the New Global Parameter
        GlobalParameter.Create(doc,aParam,ParameterType.Text)
        
        # Set the Group to Identity Data
        #Get the Parameter First
        # GROUPING NOT CURRENTLY WORKING...!!!
        #theParam = doc.GetElement(GlobalParametersManager.FindByName(doc, aParam))
        #theParam.GetDefinition().set_ParameterGroup(BuiltInParameterGroup.PG_IDENTITY_DATA)
        
        tranny.Commit()
        tranny.Dispose()
        print 'Adding Global Parameter: ' + aParam
      except Exception as e:
        print 'Ooops: \n' + e.message
        tranny.RollBack()
        tranny.Dispose()
    else:
      print 'Global Parameter Already Exists: ' + aParam
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
  
  #List for worksets we are going to create
  wslist = []
  
  #Workset Config to open the workset on creation
  wsconfig = WorksetConfiguration()

  # Make sure that each of the newWorksets are unique
  # and create them the [2:] skips the first two which
  # are created as the default worksets above
  for aWorkset in theWorksets[2:]:
    #Make sure that the work doesn't already exist
    if wst.IsWorksetNameUnique(newModel,aWorkset):
      try:
        tranny = Transaction(newModel)
        tranny.Start('Creating Workset ' + aWorkset)
        #Create the Workset
        ws = Workset.Create(newModel,aWorkset)
        tranny.Commit()
        #Add the new Workset WorksetId to the list
        wslist.Append(ws.Id)
      except Exception  as e:
        print e.message
        tranny.RollBack()
        tranny.Dispose()
    else:
      print aWorkset + ' Already Exists'
      
    #Set the new Worksets to open
    wsconfig.Open(wslist)
#-------------------------------------------------------
def setLatLon(newModel):
  print 'Setting Location'
  
  projectLocation = newModel.ActiveProjectLocation
  siteLocation = projectLocation.GetSiteLocation()

  tranny = Transaction(newModel)
  try:
    tranny.Start('Setting Coordinates')
    siteLocation.Latitude = BVN_Lat
    siteLocation.Longitude = BVN_Lon
    if tranny.HasStarted():
      tranny.Commit()
      tranny.Dispose
  except Exception as e:
    print e.message
    tranny.RollBack()
    tranny.Dispose
#-------------------------------------------------------
def createBVNModel(modelName, templateBVN):
  # Create a new model from the chosen template
  newModel = uiapp.Application.NewProjectDocument(templateBVN)
  
  # Set the Project and Global Parameters
  setParams(newModel, modelName)
  setLatLon(newModel)
  
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
def createCADLinkModel(modelName,TypeName):
  # Create a new model from the Metric "None" template
  unitsystem = UnitSystem.Metric
  newModel = uiapp.Application.NewProjectDocument(unitsystem)
  
  # Set the Project and Global Parameters
  AddBasicParameters(newModel)
  setBasicParams(newModel, modelName)
  setLatLon(newModel)
  
  # Create Worksets and make worksharing
  #makeWorkshared(newModel, modelName)
  # Enable Worksharing and create the default Worksets
  newModel.EnableWorksharing('99_LEVELS AND GRIDS',TypeName)
  
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
  relinqOptions.CheckedOutElements = True
  
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

# New Project Files
newFileBLDG = getNewfileName(BVN_Project_Number, BVN_projectAbbr, 'BUILDING')
newFileSITE = getNewfileName(BVN_Project_Number, BVN_projectAbbr, 'SITE')

# New CAD Link Files
newFileCADLinks = getCADLINKfileName(BVN_Project_Number, BVN_projectAbbr, 'CADLinks')
newFileSURVEY = getCADLINKfileName(BVN_Project_Number, BVN_projectAbbr, 'SURVEY')

# The Template File
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

# Make sure that a 'SURVEY' folder exists in the CAD Links folder
folder = getCADLinkSurveyFolder(BVN_Project_Number)
if not isValidSurveyFolder(folder):
  os.mkdir(folder)
  os.mkdir(folder + '/CAD')
else:
  if not os.path.exists(folder + '/CAD'):
    os.mkdir(folder + '/CAD')


# If ALL of the above checks are good then we can make some files
if OKtoGO:
  #Create the new Models in Project Files
  createBVNModel(newFileBLDG, templateBVN)
  createBVNModel(newFileSITE, templateBVN)

  #Create the new Models in CAD Links
  createCADLinkModel(newFileSURVEY,'SURVEY')
  createCADLinkModel(newFileCADLinks,'CADLinks')
  
  #Show when done
  ShowDone()
  

  


