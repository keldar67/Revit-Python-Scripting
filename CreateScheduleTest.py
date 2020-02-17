theSchedules = (
FilteredElementCollector(doc)
.OfCategory(BuiltInCategory.OST_Schedules)
)

#Get a Schedule view to create a New on from.
aSchedule = theSchedules.FirstElement()
#Create the New Schedule.
newSchedule = aSchedule.CreateSchedule(doc)
