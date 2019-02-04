#-----------------------------------------------------------------------------------+
def GetCellWidth(Curve):
  #Grab the curves running in a positive X direction only
  direction = XYZ(1,0,0)
  width = 0
  for c in Curve:
    if c.Direction.IsAlmostEqualTo(direction):
      width += c.Length
  
  return width * 304.8 #<---<< Convert ft to mm
#-----------------------------------------------------------------------------------+
def GetCellHeight(Curve):
  #Grab the curves running in a positive Z direction only
  direction = XYZ(0,0,1)
  height = 0
  for c in Curve:
    if c.Direction.IsAlmostEqualTo(direction):
      height += c.Length
  
  return height * 304.8 #<---<< Convert ft to mm
#-----------------------------------------------------------------------------------+
def GetCellWidthAndHeight(aCell):
  
  curves = aCell.CurveLoops
  for curve in curves:
    for edge in curve:
      ft = edge.Length
      mm = (ft * 304.8)+0.
      
      
          
  return result
#-----------------------------------------------------------------------------------+
def AnalyzeCurtainWallCell(aCell):
  result = True
  curves = aCell.CurveLoops
  for curve in curves:
    for edge in curve:
      ft = edge.Length
      mm = (ft * 304.8)+0.5
      
      if mm < minSize: result = False
          
  return result
#-----------------------------------------------------------------------------------+
def AnalyzeCurtainWall(cw):
  print 'Analyzing Curtai Wall:', cw.Id
  x = lines = cw.CurtainGrid.GetUGridLineIds().Count + 1
  y = lines = cw.CurtainGrid.GetVGridLineIds().Count + 1
  
  counter = 0
  #Get the list of cells
  theCells = cw.CurtainGrid.GetCurtainCells()
  
  #Cycle through them
  for i in range(x):
    for j in range(y):
      aCell = theCells[counter]
      
      result = AnalyzeCurtainWallCell(aCell)
      
      if False == result:
        print 'Bad Cell in Curtain Wall ' + cw.Id.ToString() + ' at Cell [' + (j+1).ToString() + ',' + (i+1).ToString() + ']'
      
      counter += 1
#-----------------------------------------------------------------------------------+

minSize = 100
minSizeft = minSize / 304.8


wall = selection[0]
grid = wall.CurtainGrid
cells = grid.GetCurtainCells()
print 'This Wall has ' + cells.Count.ToString() + ' Cells'
print 'ULines = ' + grid.NumULines.ToString()
print 'VLines = ' + grid.NumVLines.ToString()
print 'with the following panels:'
for p in grid.GetPanelIds():
  print p.ToString() + ' - ' + Element.Name.GetValue(doc.GetElement(p))