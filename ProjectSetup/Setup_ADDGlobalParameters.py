#theGlobalParameters = GlobalParametersManager.GetAllGlobalParameters(doc)
#aGlobalParameter = theGlobalParameters.ElementAt(0)

#Basic Parameters to be created in Non BVN Template Models
ParamNames = [
  'BVN_Client',
  'BVN_Project Number',
  'BVN_MM_Model Name'
]

for aParam in ParamNames:
  if GlobalParametersManager.IsUniqueName(doc,aParam):
    try:
      tranny = Transaction(doc)
      tranny.Start('Creating Global Parameter: ' + aParam)
      
      # Create the New Global Parameter
      GlobalParameter.Create(doc,aParam,ParameterType.Text)
      
      # Set the Group to Identity Data
      #Get the Parameter First
      # GROUPING NOT CURRENTLY WORKING...!!!
      #theParam = doc.GetElement(GlobalParametersManager.FindByName(doc, aParam))
      #theParam.GetDefinition().set_ParameterGroup(BuiltInParameterGroup.PG_IDENTITY_DATA)
      
      tranny.Commit()
      tranny.Dispose()
      print 'Adding Global Parameter: ' + aParam
    except Exception as e:
      print 'Ooops: \n' + e.message
      tranny.RollBack()
      tranny.Dispose()
  else:
    print 'Global Parameter Already Exists: ' + aParam