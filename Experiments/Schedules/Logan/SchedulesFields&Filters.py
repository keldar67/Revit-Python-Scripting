
bic = BuiltInCategory.OST_Schedules
aSchedule = FilteredElementCollector(doc).OfCategory(bic).FirstElement()

newSchedule = None

tranny = Transaction(doc)
try:
  tranny.Start('Creating a Schedule')
  newSchedule = aSchedule.CreateSchedule(doc,ElementId(-1))
  newSchedule.Name = 'Another Great Schedule'
  tranny.Commit()
  tranny.Dispose()
except Exception as e:
  if tranny.HasStarted:
    tranny.RollBack()
    tranny.Dispose()
  print e.message
  
#Add the Fields
SchedulableField()
newSchedule.Definition.AddField(newSField)


#------------------------------
# This bit gets the Field & Filter Information
#
#

s = selection[0]
df = s.Definition

print 'Fields'
print '======'
for i in range(0,df.GetFieldCount()): 
  f = df.GetField(i)
  name = f.GetName()
  print i.ToString() + ': ' + name + ' [' + f.FieldId.ToString() + ']'

print '\n\n'
print 'Filters'
print '======='
for x in range(0,df.GetFilterCount()): 
  fl = df.GetFilter(x)
  print x.ToString() + ': ' + '[' + fl.FilterType.ToString() + ']' + ' "' + fl.GetStringValue() + '"'