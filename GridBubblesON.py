
# Need to grab all Grids in the model

# Need to gather views that you want to turn both grid bubbles on for

# Loop for all Views

# Loop for all grids within the view and for each g in grids use the below code to turn ON both grid bubbles

# To Check if the grid/datum is visible in the view:
# if g.CanBeVisibleInView(v):
#   pass

tranny = Transaction(doc)

try:
  tranny.Start("Turning on Grid Bubbles")
  v = uidoc.ActiveView
  g.ShowBubbleInView(DatumEnds.End0,v)
  g.ShowBubbleInView(DatumEnds.End1,v)
  tranny.Commit()
  tranny.Dispose
except Exception as e:
  print e.message
  if tranny.HasStarted:
    tranny.RollBack()
    tranny.Dispose()