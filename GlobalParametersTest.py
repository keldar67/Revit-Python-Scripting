GlobalParametSet = GlobalParametersManager.GetAllGlobalParameters(doc)

for aGlobalParameter in GlobalParametSet:
  param = doc.GetElement(aGlobalParameter)
  theName = param.GetDefinition().Name
  theValue = param.GetValue().Value
  print theName + ' = ' + theValue.ToString()