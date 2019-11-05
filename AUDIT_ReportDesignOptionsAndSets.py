theOptionSets = FilteredElementCollector(doc).OfCategory(BuiltInCategory.OST_DesignOptionSets)
theOptions = FilteredElementCollector(doc).OfCategory(BuiltInCategory.OST_DesignOptions)

optionSets = {}
setCounter = 0

print 'There are [' + theOptions.Count().ToString() + '] Design Options across [' + theOptionSets.Count().ToString() + '] Desin Option Sets in this model'

for anOption in theOptions:
  #If the Design Option Set is already recorded, just add the option to it's list of options
  optionSetId = anOption.LookupParameter('Design Option Set Id').AsElementId()
  
  # Check if this is an option within an existing 
  # option set or a new option set
  if optionSetId in optionSets:
    optionSets[optionSetId].append(anOption)
  else:
    optionSets.Add(optionSetId,[])
    optionSets[optionSetId].append(anOption)

# Output the results
if optionSets.Count > 0:
  print 75 * '-'
  # Print the name of Each Option Set, then its Options
  for optionSet in optionSets:
    theOptionSet = doc.GetElement(optionSet)
    setCounter += 1
    print setCounter.ToString().zfill(2) + ') ' + theOptionSet.Name
    # Print all of the options within the Option Set
    for op in optionSets[optionSet]:
      print '\t\t+\t\t' + op.Name
    print '' # <--<< Blank line between Option Sets.