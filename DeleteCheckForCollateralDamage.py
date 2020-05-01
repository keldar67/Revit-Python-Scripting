'''
Check Element Dependancies.

Delete an element, 
capture the list of element Ids removed from the model, 
RollBack the tansaction
Check to see if the list contains more than just the element selected.
Report the elements also deleted
'''
theElements = {}
key = ''

if len(selection) > 0:
  for s in selection:
    print s.Id
    try:
      tranny = Transaction(doc)
      tranny.Start('Blah!')
      print 'Element:', s.Id, type(s)
      key = s.Id.IntegerValue
      collateraldamage = doc.Delete(s.Id)
      theElements.Add(key,collateraldamage)
      
      tranny.RollBack()
      
    except Exception as e:
      if tranny.HasStarted():
        print 'Error...!!!'
        print e.message
        tranny.RollBack()
        tranny.Dispose()        

for k in theElements.Keys:
  print  '=' * 75
  #Check to see if the list if collateral damage is
  #more than just the elements itself
  if len(theElements[k]) > 1:
    print 'If you delete Element \n[' + str(k) + '] ' + doc.GetElement(ElementId(k)).Category.Name + ' - ' + str(type(doc.GetElement(ElementId(k))))
    print 'The following Elements will also be deleted:-'  
    print
    for theId in theElements[k]:
      print str(theId) + ' - ' + doc.GetElement(ElementId(k)).Category.Name + ' - ' + str(type(doc.GetElement(theId)))
  else:
      print str(k) + ' - ' + doc.GetElement(ElementId(k)).Category.Name + ' - Clean Delete'
      
print  '=' * 75, 'FIN...'