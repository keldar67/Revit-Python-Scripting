theWarnings = doc.GetWarnings()

print 'There are ' + theWarnings.Count.ToString() + ' in this model...!'
print 75 * '-'

for aWarning in theWarnings:
  description = aWarning.GetDescriptionText()
  severity = aWarning.GetSeverity()
  wguid = msg.GetFailureDefinitionId().Guid
  
  print description
  print severity
  print wguid.ToString()
  print 75 * '-'