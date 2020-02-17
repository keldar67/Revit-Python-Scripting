﻿inplaces = (
FilteredElementCollector(doc)
.OfClass(Family)
.Where(lambda f: f.IsInPlace)
.ToList()
)

print inplaces.Count.ToString() + ' In Place Families in this Project'
print '+-----------------------------------------+'
for ip in inplaces: print ip.Name