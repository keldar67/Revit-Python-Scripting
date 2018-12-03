fec = FilteredElementCollector(doc).OfCategory(BuiltInCategory.OST_RvtLinks)
for f in fec:
  if RevitLinkInstance == type(f):
    data = Element.Name.GetValue(f).split(':')
    print data[0]
