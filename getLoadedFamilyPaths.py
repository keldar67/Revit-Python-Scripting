'''
Next stages to add the ability to move families across to the project library and re-path the familes loaded.

#
#1. Find a family that is loaded from another project
#2. Edit the family
#3. Save the family to the current/local project library
#3.01 - Check if the directory exists for the Family Category
#3.02 - If not create the directory
#4. Capture the path and close the file
#5. Reload from the captured Path into project and close
'''
#---------------------------------------------#
def getProjectPath():
  s = ''
  if not(doc.IsDetached):
    mp = doc.GetWorksharingCentralModelPath()
    s = ModelPathUtils.ConvertModelPathToUserVisiblePath(mp)
    s.Substring(0,18)
  
  return s
#---------------------------------------------#
def getProjectFromPath(thePath):
  if ':' == thePath[1]:
    result = thePath.Substring((thePath.IndexOf('\\',(thePath.IndexOf('\\')+1))+1),12)
  else:
    if '\\' == thePath.Substring(0,1):
        result = thePath.Substring(1,(thePath.IndexOf('\\',1)-1))
    else:
      result = ''

  return result

#---------------------------------------------#
def getFamilyPath(f):
  global FamiliesBadNews
  
  if isinstance(f,Family):
    fam = f
    #print 'Family'
  else:
    if isinstance(f,FamilySymbol):
      fam = f.Family
      #print 'Symbol'
    else:
      if isinstance(f,FamilyInstance):
        fam = f.Symbol.Family
        #print 'FamilyInstance'
      else:
        fam = None
  
  if None != fam:
    try:  
      famdoc = f.Document.EditFamily(fam)
      thePath = famdoc.PathName
      famdoc.Close(False)
    except:
      thePath = ''
      try:
        FamiliesBadNews.append(f.Category.Name + '|' + f.Name)
      except AttributeError:
        FamiliesBadNews.append(f.Name)
        pass
      pass
  else:
    thePath = '...'
    
  return thePath 
#---------------------------------------------#

FamiliesInPlace = []
FamiliesLoadedOK = []
FamiliesOrphaned = []
FamiliesWrongProject = []
FamiliesNotEditable = []
FamiliesBadNews = []
FamiliesCentral = []

MasterContent = '\\dc2-file001\\practice\\InfoTech\\BIM\\Revit\\RevitStandardsMasterBVN\\02_BVN_Library\\Master Content'


ProjectPath = getProjectPath()
proj = getProjectFromPath(ProjectPath)

fec = FilteredElementCollector(doc).OfClass(Family)
counter = 0

for f in fec:
  #print '-' * 75
  s = ''
  thePath = ''
  
  counter = counter + 1
  s = f.FamilyCategory.Name + '\t' + f.Name + '\t' + thePath
      
  if f.IsInPlace:
    FamiliesInPlace.append(s)  
  else:
    if f.IsEditable:
      thePath = getFamilyPath(f)
      print thePath
      
      if '' == thePath:
        FamiliesOrphaned.append(s)
      else:
        if proj == getProjectFromPath(thePath):
          FamiliesLoadedOK.append(s)
        else:
          print 'Current Family: ' + thePath
          print getProjectFromPath(thePath)
          s = f.FamilyCategory.Name + '\t' + f.Name + '\t' + getProjectFromPath(thePath) + '\t' + thePath
          if MasterContent.ToLower() in thePath.ToLower():
            FamiliesCentral.append(s)
          else:
            FamiliesWrongProject.append(s)
    else:
      FamiliesNotEditable.append(f.Name)
      
print '-_' * 50
print 'There are ' + str(FamiliesNotEditable.Count) + 'None Editable Families in the project'
for f in FamiliesNotEditable: print f
print '-' * 40
print 'There are ' + str(FamiliesInPlace.Count) + ' In Place Families in the project'
for f in FamiliesInPlace: print f
print '-' * 40
print 'There are ' + str(FamiliesCentral.Count) + ' Families Loaded from Master Content'
print '-' * 40
print 'There are ' + str(FamiliesLoadedOK.Count) + ' Families Loaded from within the project number: ' + getProjectFromPath(ProjectPath)
print '-' * 40
print 'There are ' + str(FamiliesOrphaned.Count) + ' Orphaned Families in the Model.'
for f in FamiliesOrphaned: print f
print '-!_' * 50
print 'There are ' + str(FamiliesWrongProject.Count) + ' Families Loaded from other Projects as follows:'
print 'Category\tFamilyName\tProjectNumber\tFilePath' 
for f in FamiliesWrongProject: print f
print '-' * 40
print 'The following Families need looking at for potential corruption'
for f in FamiliesBadNews: print f
print '-!_' * 50
    
    #print str(counter)
    #print f.FamilyCategory.Name
    #print f.Name
    #print thePath
