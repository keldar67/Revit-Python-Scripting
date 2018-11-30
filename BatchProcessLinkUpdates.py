basepath = r'X:\BIM\5.0 Project Resources\Ian\TEST'

themodels = [
'TEST-01.rvt',
'TEST-02.rvt',
'TEST-03.rvt',
'TEST-04.rvt'
]

thepaths = []

app = uiapp.Application
class SynchLockCallback(ICentralLockedCallback):
  def ShouldWaitForLockAvailability():
    return False
#--------------------------------------------------------------------------------#
# Refer to https://knowledge.autodesk.com/search-result/caas/CloudHelp/cloudhelp/2016/ENU/Revit-API/files/GUID-F99FBBCC-AE58-46F5-85AF-0A7C3C5C0576-htm.html?_ga=2.18634043.303903109.1543365649-1865787168.1469580492
#--------------------------------------------------------------------------------#
def GetLocalFilePath(filename):

  #If we get a filename including the ".rvt" then remove it.
  if filename.EndsWith('.rvt'):
    fname = filename[:-4]
  else:
    fname = filename
  
  localpath = "C:\\REVIT_LOCAL" + app.VersionNumber + "\\" + fname + "_" + app.Username + ".rvt."
  
  return localpath
#--------------------------------------------------------------------------------#
def DoIt():
  #Handle to the Application
  app = uiapp.Application
  
  #Arguments required for the file open operation.
  modelPath = ModelPathUtils.ConvertUserVisiblePathToModelPath(apath)
  opts = OpenOptions()
  opts.DetachFromCentralOption = DetachFromCentralOption.DoNotDetach
  #Open the Document.
  currentdoc = uiapp.Application.OpenAndActivateDocument(modelPath,opts,False)
  
  #Setup the Transaction Options for the Synchronize
  transOpts = TransactWithCentralOptions()
  transCallback = SynchLockCallback()
  transOpts.SetLockCallback(transCallback)
  
  #Setup the Synchronization Options for the Synchronize
  syncOpts = SynchronizeWithCentralOptions()
  relinquishOpts = RelinquishOptions(True)
  syncOpts.SetRelinquishOptions(relinquishOpts)
  syncOpts.SaveLocalAfter = True
  syncOpts.Comment = 'Automated Revit Links update'
  
  #Synchronize the Document
  try:
    currentdoc.SynchronizeWithCentral(transOpts,syncOpts)
  except Exception as e:
    print 'Synchronization Failed:'
    print e.message
  
  #Then Close the Document
  currentdoc.Close(True)
  print 'Closed document: ' + apath
#--------------------------------------------------------------------------------#
for amodel in themodels:
  thepath = '\\'.join([basepath, amodel])
  thepaths.Add(thepath)
  
for apath in thepaths:
  print 'Opening document: ' + apath
  DoIt()
