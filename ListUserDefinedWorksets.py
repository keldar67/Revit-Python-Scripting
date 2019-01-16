wst = doc.GetWorksetTable()

theWorksets = (
FilteredWorksetCollector(doc)
.Where(lambda w: w.Kind == WorksetKind.UserWorkset)
)

print ' +------------+-------------------------------------------+'
for aWorkset in theWorksets:
  print ' | ' + aWorkset.Id.ToString().ljust(10) + ' | ' + aWorkset.Name
print ' +------------+-------------------------------------------+'