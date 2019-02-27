theFamilys = FilteredElementCollector(doc).OfClass(Family).OrderBy(lambda f: f.FamilyCategory.Name)

for aFamily in theFamilys:
  if aFamily.FamilyCategory is not None:
    cat = aFamily.FamilyCategory.Name
  else: 
    cat = 'None'
  name = Element.Name.GetValue(aFamily)
  if type(aFamily) != None:
    print cat + "\t" + name