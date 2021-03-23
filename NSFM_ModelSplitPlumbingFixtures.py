import clr
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import BuiltInParameter
from System import Enum

key = 'FAMILY_HOSTING_BEHAVIOR'

names = Enum.GetNames(BuiltInParameter)
values = Enum.GetValues(BuiltInParameter)

bip_dict = dict(zip(names, values))
# Returns a BuiltInParameter given its name (key)
bip = bip_dict[key]

# For above solution 
# See: https://forum.dynamobim.com/t/setting-built-in-parameter-by-using-a-variable-value/49466


# Get the Plumbing Fixtures from the model.
pfs = (FilteredElementCollector(doc)
  .OfCategory(BuiltInCategory.OST_PlumbingFixtures)
  .WhereElementIsNotElementType()
  .ToList()
)


# Loop through them and check the BuiltInParameter for Hosting Behaviour
# Looking for Floor Hosted families only
i = 0
for pf in pfs:
  i += 1
  print i
  hosting = pf.Parameter[bip]
  print type(hosting)
  if (not type(hosting).Equals(None)
    and
    hosting.HasValue
    and
    # Face Hosted Families Only
    hosting.Equals(FamilyHostingBehavior.Face)
    ):
    print pfs.Count()