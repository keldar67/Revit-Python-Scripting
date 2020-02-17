#================================================================================#
#      _____               __                            
#      \_   \__ _ _ __     \ \  __ _ _ __ ___   ___  ___ 
#       / /\/ _` | '_ \     \ \/ _` | '_ ` _ \ / _ \/ __|
#    /\/ /_| (_| | | | | /\_/ / (_| | | | | | |  __/\__ \
#    \____/ \__,_|_| |_| \___/ \__,_|_| |_| |_|\___||___/
#
#  Title: StructureAnalyticsOFF.py
#
#  Description: Turns off the Boolean parameter 'Enable Analytical Model'
#               for Structural Categories: Columns, Foundations & Framing
#  
#
#  Date: 20th January 2020
#
#================================================================================#
import time

#------------------------------------------------------------------------------------#
def processThings(theThings, thingName):

  thingsSuccess = []
  thingsNoParam = []
  thingsFailed = []
  thingsNoChange = []
  i = 0
  count = theThings.Count.ToString()
  start = time.time()
  
  for aThing in theThings:
    i += 1
    #print i.ToString() + ' of ' + count + ' ' + thingName
    id = aThing.Id.ToString()
    
    p = aThing.LookupParameter('Enable Analytical Model')
    if p:
      if p.AsValueString().Equals('Yes'):
        #print 'Element Id [' + id + '] Changing From: ' + p.AsValueString() + ' to No/False'
        tranny = Transaction(doc)
        try:
          tranny.Start('Switching Off analytics')
          p.Set(False)
          tranny.Commit()
          tranny.Dispose()
          thingsSuccess.append(id)
        except Exception as e:
          if tranny.HasStarted:
            tranny.RollBack()
            tranny.Dispose()
          print 'Something Went Wrong'
          print e.message
          thingsFailed.Add(id)
      else:
        thingsNoChange.Add(id)
    else:
      thingsNoParam.Add(id)
      #print "Column [" + id + "] Doesn't have the parameter"
  end = time.time()
  duration = end - start
  print 'Results for type: ' + thingName + ' Processed in ' + duration.ToString() + ' seconds'
  print '------------------------------------------'
  print 'Parameters Changed  : ' + thingsSuccess.Count.ToString()
  print 'Failed Changes      : ' + thingsFailed.Count.ToString()
  print 'No Change Required  : ' + thingsNoChange.Count.ToString()
  print 'Parameter Not Found : ' + thingsNoParam.Count.ToString()
  print '=========================================='
  
#------------------------------------------------------------------------------------#
def main():

  #Get the Structural Columns
  theColumns = (
  FilteredElementCollector(doc)
  .OfCategory(BuiltInCategory.OST_StructuralColumns)
  .ToList()
  )
    
  processThings(theColumns, 'Column')
  #---------------------
  
  #Get the Structural Framing
  theStructuralFraming = (
  FilteredElementCollector(doc)
  .OfCategory(BuiltInCategory.OST_StructuralFraming)
  .ToList()
  )
  
  processThings(theStructuralFraming, 'Framing')
  #---------------------
  
  #Get the Structural Foundations
  theStructuralFoundations = (
  FilteredElementCollector(doc)
  .OfCategory(BuiltInCategory.OST_StructuralFoundation)
  .ToList()
  )
  
  processThings(theStructuralFoundations, 'Foundation')
  #---------------------
#------------------------------------------------------------------------------------#
if __name__ == '__main__': main()
