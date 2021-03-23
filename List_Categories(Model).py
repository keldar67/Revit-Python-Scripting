cats = []

for cat in doc.Settings.Categories:
  if cat.CategoryType == CategoryType.Model:
    cats.Add(cat.Name)
  
for acat in sorted(cats): print acat