dg = selection[0]

import pprint
pp = pprint.PrettyPrinter()

ids = dg.GetMemberIds()
elems = {}

for id in ids:
  elem = doc.GetElement(id)
  typeName = elem.GetType().Name
  print typeName
  if typeName in elems.Keys:
    elems[typeName].append(id)
  else:
    elems.Add(typeName,[])
    elems[typeName].Append(id)
    
pp.pprint(elems)

for akey in elems:
  print akey + ' : ' + elems[akey].Count.ToString()