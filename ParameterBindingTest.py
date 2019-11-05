theCategory = BuiltInCategory.OST_Doors

theElements = FilteredElementCollector(doc).OfCategory(theCategory)

anElement = theElements.FirstElement()

theParams = anElement.GetOrderedParameters()

for aParam in theParams: 
  prefix = ''
  guid = ''
  
  if aParam.IsShared:
    prefix = 'S'
    guid = '[' + aParam.GUID.ToString() + ']'
  if not aParam.UserModifiable:
    prefix = 'B'
    
  print prefix + ':' + aParam.Definition.Name + ' - ' + guid
  

