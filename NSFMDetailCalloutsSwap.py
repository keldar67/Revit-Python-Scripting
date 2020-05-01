theViews = (
FilteredElementCollector(doc)
.OfCategory(BuiltInCategory.OST_Views)
.Where(lambda v: 
  v.ViewType.Equals(ViewType.Detail)
  and
  '63F - CORES, STAIRS & LIFTS - PLANS' in v.LookupParameter('BVN Alphabet').AsString()
  )
.ToList()
)

print theViews.Count.ToString() + ' Views Found'
print '-' * 50

for aView in theViews: print aView.ViewName