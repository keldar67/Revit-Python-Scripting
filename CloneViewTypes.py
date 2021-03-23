#---------------------------------------------------------------#
#
# Pre-requisites:
# ---------------
#
#  1.
#  You need to have already transferred your view templates
#  using Transfer Project Standards so that this script can
#  match up the default templates when re-creating the view
#  types in this file.
#
#---------------------------------------------------------------#

sourcedocName = 'Project1'

#---------------------------------------------------------------#
def getSourceProject(sourcedocName):
  app = doc.Application
  #Loop through all open documents searching for a match
  for adoc in app.Documents:
    #If we find a match return the document
    if adoc.Title.Equals(sourcedocName):
      return adoc
      
  return false
#---------------------------------------------------------------#
def findMatchingLocalViewType(remoteType):
  viewtypes = (
    FilteredElementCollector(doc)
    .OfClass(type(remoteType))
    )
  
  print 'viewtypes count = ' + viewtypes.Count().ToString()

  x = viewtypes.FirstElement()
  
  if x:
    return x
  else:
    return None
#---------------------------------------------------------------#
def findMatchingTemplateByName(templateName):
  localtemplates = (
    FilteredElementCollector(doc)
    .OfCategory(BuiltInCategory.OST_Views)
    #.Where(lambda v: v.IsTemplate)
    )
    
  print localtemplates.Count().ToString() + ' local View templates'
  for aViewTemplate in localtemplates:
    if aViewTemplate.Name.Equals(templateName):
      return aViewTemplate
      
  #If we get here we didn't find a match
  return false
#---------------------------------------------------------------#
def cloneViewType(viewtype):
  #Get the default template for the view type.
  param = viewtype.LookupParameter('View Template applied to new views')
  
  #Check the the parameter exists and has a value.
  if param and param.HasValue:
    vtId = param.AsElementId()
    #Next make sure that it is a valid template ID
    if vtId == ElementId.InvalidElementId:
      print 'No Default Template'
    else:
      #Get the Template
      template = sourcedoc.GetElement(vtId)
      #Get the Template Name
      templateName = Element.Name.GetValue(template)
      #search for a template in the local document with the corresponding name
      templatelocal = findMatchingTemplateByName(templateName)
      viewtypelocal = findMatchingLocalViewType(viewtype)
      
      print '... ' + viewtypelocal.FamilyName
      #createNewViewType(typeName, defaultTemplate, CalloutType)
  else:
    print 'Param Not Found'
  
  

#---------------------------------------------------------------#
def getSourceViewTypes(sourcedoc):
  theTypes = (FilteredElementCollector(sourcedoc)
    .OfClass(ViewFamilyType)
    .OrderBy(lambda t: t.FamilyName)
    .ToList()
    )

  for aType in theTypes: 
    print aType.FamilyName + " -- " + Element.Name.GetValue(aType)
    param = aType.LookupParameter('View Template applied to new views')
    if param and param.HasValue:
      vtId = param.AsElementId()
      if vtId == ElementId.InvalidElementId:
        print 'No Default Template'
      else:
        template = sourcedoc.GetElement(vtId)
        print 'Template: ' + template.ToString()
        templateName = Element.Name.GetValue(template)
        print 'Template Name: ' + templateName
        
        print '... cloning view type...'
        cloneViewType(aType)
    else:
      print 'Param Value Not Found'
    print '\n'
#---------------------------------------------------------------#

#Try and Get the Source Document
sourcedoc = getSourceProject(sourcedocName)

if sourcedoc:
  #Get the Source Views
  getSourceViewTypes(sourcedoc)
  
else:
  print 'Source Document Not Found'