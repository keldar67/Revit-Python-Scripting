# Before running this script, select a Door family in the Model.

d = selection[0]
builtin = []
shared = []
others = []

pset = d.Parameters

print 'Analyzing ' + pset.Size.ToString() + ' parameters'

for p in pset:
  print p.Definition.Name
  if p.IsShared:
    shared.append(p)
  elif not p.Definition.BuiltInParameter == BuiltInParameter.INVALID:
    builtin.append(p)
  else:
    others.append(p)

print 50 * '='
print 'Built In Parameters = ' + builtin.Count.ToString()
for p in builtin: print p.Definition.Name
print 50 * '-'
print 'Shared Parameters   = ' + shared.Count.ToString()
for p in shared: print p.GUID.ToString() + '\t' + p.Definition.Name
print 50 * '-'
print 'Other Parameters   = ' + others.Count.ToString()
for p in others: print p.Definition.Name
print 50 * '-'

