theColumns = (
  FilteredElementCollector(doc)
  .OfCategory(BuiltInCategory.OST_StructuralColumns)
  .ToList()
)
i = 0
count = theColumns.Count.ToString()

for aColumn in theColumns:
  i += 1
  print i.ToString() + ' of ' + count + ' Columns'
  id = aColumn.Id.ToString()
  
  p = aColumn.LookupParameter('Enable Analytical Model')
  if p:
    print 'Element Id [' + id + '] Changing From: ' + p.AsValueString() + 'No/False'
    tranny = Transaction(doc)
    try:
      tranny.Start('Switching Off analytics')
      p.Set(False)
      tranny.Commit()
      tranny.Dispose()
      print 'Success!'
    except Exception as e:
      if tranny.HasStarted:
        tranny.RollBack()
        tranny.Dispose()
      print 'Something Went Wrong'
      print e.message
  else:
    print "Column [" + id + "] Doesn't have the parameter"
    