
DesignStage = '⓿ DOCUMENTATION NEW'

theViews = (FilteredElementCollector(doc)
  .OfClass(ViewPlan)
  .WhereElementIsNotElementType()
  # Get only the views where the Design Stage Parameter matches the above
  .Where(lambda v: ((not v.IsTemplate) and (v.ViewType == ViewType.FloorPlan) and (v.LookupParameter('Design Stage').AsString().Equals(DesignStage))))
  #.ToList()
  )
  
#print theViews.Count().ToString() + ' Views Found'
count = 0  
for aView in theViews:
  if aView:
    print aView.Id
    try:
      count += 1
      print count.ToString() + ' - ' + aView.LookupParameter('BVN Alphabet').AsString() + " | " + aView.Name
      
    except Exception as e:
      print count
      print e.message
      
      