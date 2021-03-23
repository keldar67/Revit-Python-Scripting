#========================================================================#
#      _____               __                            
#      \_   \__ _ _ __     \ \  __ _ _ __ ___   ___  ___ 
#       / /\/ _` | '_ \     \ \/ _` | '_ ` _ \ / _ \/ __|
#    /\/ /_| (_| | | | | /\_/ / (_| | | | | | |  __/\__ \
#    \____/ \__,_|_| |_| \___/ \__,_|_| |_| |_|\___||___/
#
#
#  The Script pushes information into Global Parameters and 
#  Project Parameters at the same time making sure that the 
#  Job Number, Name & Client Information are consistent and also 
#  complete in the file.
#
#  Feb 2020
#
#================ EDIT THESE VALUES BEFORE RUNNING ======================#
BVN_Project_Name = "UTAS STONE & ARCHITECTURE".upper()
BVN_Project_Number = "2005012".upper()
BVN_Client = "University of Tasmania".upper()
BVN_Client_ProjectNumber = "TBC".upper()
BVN_Project_Type = "EDUCATION".upper()
BVN_Building_Name = "FURNITURE SCHOOL".upper()
BVN_MM_Model_Name = "FURNITURE SCHOOL".upper()
#========================================================================#
def setGlobalParameter(pname, pvalue):
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
def setProjectParameter(pname, pvalue):
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
def ShowDone():
  print('\n')
  print('  ____   ___  _   _ _____       _ ')
  print(' |  _ \ / _ \| \ | | ____|     | |')
  print(' | | | | | | |  \| |  _|       | |')
  print(' | |_| | |_| | |\  | |___ _ _ _|_|')
  print(' |____/ \___/|_| \_|_____(_|_|_|_)')
  print('\n')
#-------------------------------------------------------
#Set Global Parameters
setGlobalParameter("BVN_Project Name", BVN_Project_Name)
setGlobalParameter("BVN_Project Number", BVN_Project_Number)
setGlobalParameter("BVN_Client", BVN_Client)
setGlobalParameter("BVN_MM_Model Name", BVN_MM_Model_Name)

#Set Project Parameters
setProjectParameter("Client Name", BVN_Client)
setProjectParameter("Project Name",BVN_Project_Name)
setProjectParameter("Project Number",BVN_Project_Number)
setProjectParameter("Building Name",BVN_Building_Name)
setProjectParameter("Original Model By","BVN")
setProjectParameter("Project Type", BVN_Project_Type)
setProjectParameter("Client Project Number",BVN_Client_ProjectNumber)

ShowDone()



