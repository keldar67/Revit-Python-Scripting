blocks = (
FilteredElementCollector(doc)
.OfCategory(BuiltInCategory.OST_TitleBlocks)
)

for b in blocks: print Element.Name.GetValue(b.Family)

