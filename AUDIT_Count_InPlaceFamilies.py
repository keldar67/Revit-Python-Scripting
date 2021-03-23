inplaces = (
FilteredElementCollector(doc)
.OfClass(Family)
.Where(lambda f: f.IsInPlace)
.OrderBy(lambda c: c.FamilyCategory.Name)
.ToList()
)

print '+--------------------------------------------------------------------------+'
print '| ' + inplaces.Count.ToString() + ' In Place Families in this Project'
print '+----------------------+---------------------------------------------------+'
for ip in inplaces: 
  print '| ' + ip.FamilyCategory.Name.ljust(20) + ' | ' + ip.Name.ljust(50) + '|'
  
print '+----------------------+---------------------------------------------------+'