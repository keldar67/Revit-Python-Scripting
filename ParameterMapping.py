bic = BuiltInCategory.OST_Doors

map = doc.ParameterBindings
it = map.ForwardIterator
it = map.ForwardIterator()

while it.MoveNext():
  if it.Current.Categories.Contains(cat):
    print it.Key
    print it.Key.Name
    for c in it.Current.Categories:
      print c.Name
    print '-' * 50
    