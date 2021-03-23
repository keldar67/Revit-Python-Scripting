theCats = []

for cat in doc.Settings.Categories:
  theCats.append(cat.Name.ToString())
  #print cat.Name

theCats.sort()
for aCat in theCats:
  print aCat