#------------------------------------------------------------------------#
#
#  This script will read all view types in the model and produce a
#  TAB separated list in the console above that can be pasted into 
#  Excel using the "Paste Special" option
#  Fields as follows:-
#     - Family Name
#     - Type Name
#     - Default Template ID
#     - Default Template Name
#     - Dependant on Template Boolean
#     - Callout Tag
#
#------------------------------------------------------------------------#

theViewTypes = ( 
  FilteredElementCollector(doc)
  .OfClass(ViewFamilyType)
  .OrderBy(lambda v: v.FamilyName)
  )
  
for aViewType in theViewTypes:
  
  #Get the Family Type
  textfamilyName = aViewType.FamilyName
  
  #Get the Type Name
  texttypeName = Element.Name.GetValue(aViewType)
  
  #Get Reference Label
  param = aViewType.LookupParameter('Reference Label')
  if param and param.HasValue:
    referencelabel = param.AsString()
  else:
    referencelabel = ''
    
  #Get the Default Template Parameter
  param = aViewType.LookupParameter('View Template applied to new views')
  if param and param.HasValue:
    defaultTemplateId = param.AsElementId()
    if defaultTemplateId == ElementId.InvalidElementId:
      defaultTemplate = 'No Element Id'
      templateName = ''
    else:
      # If we get here then 
      # there is a vaild template specified
      defaultTemplate = param.AsElementId().ToString()
      template = doc.GetElement(defaultTemplateId)
      templateName = Element.Name.GetValue(template)
  else:
    defaultTemplate = 'No default Template'
    templateName = ''
    
  #Get the Apply to New Views Parameter Value
  param = aViewType.LookupParameter('New views are dependent on template')
  if param and param.HasValue:
    dependantOnTemplate = param.AsValueString()
  else:
    dependantOnTemplate = ' None '
    
  #Get Callout Tag Info
  param = aViewType.LookupParameter('Callout Tag')
  if param and param.HasValue:
    calloutTag = param.AsValueString()
  else:
    calloutTag = ' None '
  
  print textfamilyName + '\t' + texttypeName + '\t' + referencelabel + '\t' + defaultTemplate + '\t' + templateName + '\t' + dependantOnTemplate + '\t' + calloutTag