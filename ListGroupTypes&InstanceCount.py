

theDetailGroups = (
  FilteredElementCollector(doc)
  .OfCategory(BuiltInCategory.OST_IOSDetailGroups)
  .Where(lambda dg: type(dg) == Group) #<-- Filter Just Group Instances
  .OrderBy(lambda dg: Element.Name.GetValue(dg))
  )

theModelGroups = (
  FilteredElementCollector(doc)
  .OfCategory(BuiltInCategory.OST_IOSModelGroups)
  .Where(lambda mg: type(mg) == Group) #<-- Filter Just Group Instances
  .OrderBy(lambda mg: Element.Name.GetValue(mg))
  )

detGroupInstances = {}
modGroupInstances = {}
#----------------------------------------------------------------------------------------
print '==== DETAIL GROUPS ===='

if theDetailGroups.Count() > 0:
  for aDetGroup in theDetailGroups:
    print type(aDetGroup)
    if not(aDetGroup.Name in detGroupInstances):
      #Create a new entry in the dictionary if it doesn't exist
      #Using the Group Name as the Key
      detGroupInstances.Add(aDetGroup.Name,[])
      #Add the ElementId of this first instance of this group to the list in the dict.
      detGroupInstances[aDetGroup.Name].append(aDetGroup.Id)
    else:
      #If the group type already exists within the dictionary, just add the ElementId
      detGroupInstances[aDetGroup.Name].append(aDetGroup.Id)
  
  #Print the dictionary out
  for k,v in detGroupInstances.iteritems():
    #Group Name followed by the number of instances
    print k + ' [' + v.Count.ToString() + ']'
  print '==== ' + theDetailGroups.Count().ToString() + ' instances in ' + detGroupInstances.Keys.Count.ToString() + ' Detail Group Types ====\n'

else:
  print 'No Detail Groups in the Model'    

#----------------------------------------------------------------------------------------
print '==== MODEL GROUPS ===='
 
if theModelGroups.Count() > 0:
  for aModGroup in theModelGroups:
    print type(aModGroup)
    if not(aModGroup.Name in modGroupInstances):
      #Create a new entry in the dictionary if it doesn't exist
      #Using the Group Name as the Key
      modGroupInstances.Add(aModGroup.Name,[])
      #Add the ElementId of this first instance of this group to the list in the dict.
      modGroupInstances[aModGroup.Name].append(aModGroup.Id)
    else:
      #If the group type already exists within the dictionary, just add the ElementId
      detGroupInstances[aModGroup.Name].append(aModGroup.Id)
  
  #Print the dictionary out
  for k,v in modGroupInstances.iteritems():
    #Group Name followed by the number of instances
    print k + ' [' + v.Count.ToString() + ']'
  print '==== ' + theModelGroups.Count().ToString() + ' instances in ' + modGroupInstances.Keys.Count.ToString() + ' Model Group Types ====\n'

else:
  print 'No Model Groups in the Model' 
#----------------------------------------------------------------------------------------