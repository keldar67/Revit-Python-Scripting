plans = (FilteredElementCollector(doc)
  .OfClass(ViewPlan)
  .Where(lambda v: v.ViewType == ViewType.FloorPlan and (v.LookupParameter('Design Stage').HasValue and v.LookupParameter('Design Stage').AsString().EndsWith('DOCUMENTATION NEW')))
  )
for p in plans: 
  ds = p.LookupParameter('Design Stage').AsString() if p.LookupParameter('Design Stage').HasValue else "None"
  alphabet = p.LookupParameter('BVN Alphabet').AsString() if p.LookupParameter('BVN Alphabet').HasValue else "None"
  vName = p.Name if type(p.Name) != None else "No Name"
  vType = p.ViewType.ToString() if type(p.ViewType) == ViewType else "NoneType"
  if p:
    print vType + "\t" + vName + "\t" + ds + "\t" + alphabet