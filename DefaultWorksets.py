#Global Variables  
theWorksets = 0
wst = 0
AuditViewPrefix = '3DAV•WS - '

#The New Worksets
nw = []

nw.append('00_FACADE')
nw.append('10_STRUCTURE')
nw.append('20_VERTICAL CIRCULATION')

nw.append('30_INTERIOR')
nw.append('40_FF&E')
nw.append('50_SITE')

nw.append('51_ENTOURAGE')
nw.append('60_MASSING')

#nw.append('70_SAFETY IN DESIGN')

nw.append('90_LINK_BVN SITE')
nw.append('90_LINK_BVN BUILDING')

nw.append('91_LINK_CONSULT_CONSULTANT_01')
nw.append('91_LINK_CONSULT_CONSULTANT_02')

nw.append('92_LINK_CAD HOST MODEL 01')
nw.append('92_LINK_CAD HOST MODEL 02')

#------------------------------------------------------------------------------------#
def Create3DAuditView(worksetname):
  global AuditViewPrefix
  
  fec = FilteredElementCollector(doc).OfClass(ViewFamilyType).ToElements()
  for f in fec:
    if f.ViewFamily == ViewFamily.ThreeDimensional:
       vft = f
  tranny = Transaction(doc)
  tranny.Start('Creating 3D View')
  if tranny.HasStarted:
    print 'Creating Audit View: ' + AuditViewPrefix + worksetname
    myView = View3D.CreateIsometric(doc, vft.Id)
    myView.Name = AuditViewPrefix + worksetname
    myView.Parameter['BVN Alphabet'].Set('Audit Views')
    myView.Parameter['Design Stage'].Set('000 Model Management')
    tranny.Commit()
    tranny.Dispose()
    #uidoc.ActiveView = myView
  return myView
  
#------------------------------------------------------------------------------------#
def CreateAuditViews():
  global nw
  global AuditViewPrefix
  
  worksets = FilteredWorksetCollector(doc).OfKind(WorksetKind.UserWorkset)
  existingViewNames = []
  existingViews = FilteredElementCollector(doc).OfClass(View)
  for v in existingViews: 
    existingViewNames.append(v.Name)
  
  for theName in nw:
    fullname = AuditViewPrefix + theName
    #Check if View AlreadyExists with this name
    if fullname in existingViewNames:
      print '3DView already exists: ' + fullname    
    else:
      
      print 'Creating AuditView'
      #Create The View
      wsView = Create3DAuditView(theName)
      try:
        tranny = Transaction(doc)
        tranny.Start('Hiding Worksets')
        if Tranny.HasStarted:   
          #Turn off the other worksets in this view
          for w in worksets:
            if w.Name == theName:
              wsView.SetWorksetVisibility(w.Id, WorksetVisibility.Visible) #ON
            else:
              wsView.SetWorksetVisibility(w.Id, WorksetVisibility.Hidden) #OFF
        tranny.Commit()
        tranny.Dispose()        
      except Exception, e:
        if tranny.HasStarted:
          tranny.RollBack()
          tranny.Dispose()
       
#------------------------------------------------------------------------------------#
def getWorksetByName(name):
  global theWorksets
  
  result = False
  
  for w in theWorksets:
    if name == w.Name:
      result = w
  
  return result
#------------------------------------------------------------------------------------#
def initialise():
  global theWorksets
  global wst
  if doc.IsWorkshared:
    mp = doc.GetWorksharingCentralModelPath()
    theWorksets = WorksharingUtils.GetUserWorksetInfo(mp)
    
    wst = doc.GetWorksetTable()
    return True
  else:
    return False
#------------------------------------------------------------------------------------#
def RenameWS(ws, newName):
  global wst
  try:
    msg = 'Renaming ' + ws.Name + ' to ' + newName
    tranny = Transaction(doc)
    tranny.Start(msg)
    
    wst.RenameWorkset(doc, ws.Id, newName)
    print msg
    tranny.Commit()
  except Exception, e:
    print 'Failed to rename ' + ws.Name + ' as ' + newName
    print e.message
    if tranny.HasStarted: tranny.RollBack()
#------------------------------------------------------------------------------------#  
def CreateWS(name):
  if wst.IsWorksetNameUnique(doc,name):
    try:
      msg = 'Creating Workset: ' + name
      tranny = Transaction(doc)
      tranny.Start(msg)
      
      ws = Workset.Create(doc, name)
      print msg
  
      tranny.Commit()
    except Exception, e:
      print 'Failed to Create: ' + name
      print e.message
      if tranny.HasStarted: tranny.RollBack()
  else:
      print 'Workset: ' + name + ' already exists in ' + doc.Title

#------------------------------------------------------------------------------------#  
  
def main():
  global nw
  lg = -1
  w1 = -1
  
  if initialise():
    #Rename the two default Worksets
    lg = getWorksetByName('Shared Levels and Grids')
    if lg:
      RenameWS(lg, '99_LEVELS AND GRIDS')
      
    #Create The Worksets  
    for n in nw:
      CreateWS(n)
      
    #Create Audit Views for Each Workset
    #CreateAuditViews()

  else:
    print 'Sorry this file is not workset enabled'
  
  

#Launch the program
if __name__ == "__main__":
  main()
  
  
  
  