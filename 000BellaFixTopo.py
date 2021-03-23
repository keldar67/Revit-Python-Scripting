class MyFailureProcessor(IFailuresPreprocessor):
  def __init__(self):
    pass
  def PreprocessFailures(self,failuresAccessor):
    return FailureProcessingResult.Continue
    
aFoot =304.8
topo = selection[0]

#topo = doc.GetElement(ElementId(2540544))
#Get The Internal Points
intPoints = topo.GetInteriorPoints()
extPoints = topo.GetBoundaryPoints()

#Merge the lists of points
thePoints = intPoints.Concat(extPoints)

tranny = Transaction(doc)
failProc = MyFailureProcessor()

try:
  #Create a TopographyEditScope which encapsulates the inner 
  #Transactions like a Transaction Group.
  scope = TopographyEditScope(doc, 'MovingPoints')
  print 'starting edit scope'
  
  #Start the TopographyEditScope
  scope.Start(topo.Id)
  print 'started'
  tranny.Start('Moving Point')
  #Check and Fix each point
  for aPoint in thePoints:
    
    #Convert the points from feet to meters
    z = aPoint.Z * aFoot
    print 'Old Zed = ' + z.ToString()
    
    #If the point hasn't already been corrected
    if z < 1000:
      newz = z * 1000 / aFoot
      print 'New Zed = ' + newz.ToString()
      
      #Calculate the new Elevation
      movedPoint = XYZ(aPoint.X, aPoint.Y, aPoint.Z)
      targetPoint = XYZ(aPoint.X, aPoint.Y, newz)
      
      topo.ChangePointElevation(movedPoint, newz)
      
  tranny.Commit()
  scope.Commit(failProc)
  
except Exception as e:
  #Roll Back the Transaction if it is still open.
  if tranny.HasStarted():
    tranny.RollBack()
    tranny.Dispose()
  #Close the TopographyEditScope if it is still open.
  if scope.IsActive:
    scope.Commit(failProc)
  print 'Oooops'
  print e.message
  print aPoint