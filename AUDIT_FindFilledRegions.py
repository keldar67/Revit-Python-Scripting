Regions = (
FilteredElementCollector(doc)
.OfCategory(BuiltInCategory.OST_DetailComponents)
.Where(lambda fr: FilledRegion == type(fr))
)

Masking = Regions.Where(lambda fr: 'Masking Region'.Equals(fr.LookupParameter('Type Name').Element.Name))
Filled = Regions.Where(lambda fr: 'Detail Filled Region'.Equals(fr.LookupParameter('Type Name').Element.Name))

print 'Filled Regions : ' + Filled.Count().ToString()
print 'Masking Regions: ' + Masking.Count().ToString()
print '                 --------'
print 'Total Regions  : ' + filledRegion.Count().ToString()
