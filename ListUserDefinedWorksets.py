wst = doc.GetWorksetTable()

theWorksets = (
FilteredWorksetCollector(doc)
.Where(lambda w: w.Kind == WorksetKind.UserWorkset)
.OrderBy(lambda w: w.Name)
)

print ' +------------+-------------------------------------------+'
for aWorkset in theWorksets:
  print ' | ' + aWorkset.Id.ToString().ljust(10) + ' | ' + aWorkset.Name
print ' +------------+-------------------------------------------+'