﻿
#========================================================================#
#      _____               __                            
#      \_   \__ _ _ __     \ \  __ _ _ __ ___   ___  ___ 
#       / /\/ _` | '_ \     \ \/ _` | '_ ` _ \ / _ \/ __|
#    /\/ /_| (_| | | | | /\_/ / (_| | | | | | |  __/\__ \
#    \____/ \__,_|_| |_| \___/ \__,_|_| |_| |_|\___||___/
#
#
#  The Script makes a saved as a workshared model and 
#  creates default worksets
#
#
#  May 2020
#
#========================================================================#
import datetime

#The default worksets for a Building Model
newWorksets = [
'50_SITE BOUNDARY',
'51_ENTOURAGE',
'60_MASSING',
'70_SAFETY IN DESIGN',
'90_LINK_BVN_BUILDING',
'92_LINK_CAD_SURVEY'
]
#-------------------------------------------------------
def ShowDone():
  print('\n')
  print('  ____   ___  _   _ _____       _ ')
  print(' |  _ \ / _ \| \ | | ____|     | |')
  print(' | | | | | | |  \| |  _|       | |')
  print(' | |_| | |_| | |\  | |___ _ _ _|_|')
  print(' |____/ \___/|_| \_|_____(_|_|_|_)')
  print('\n')
#-------------------------------------------------------
#If the model isn't already workshared then
# Collaborate it on the Network with standard default and Grid & Levels Worksets
if not doc.IsWorkshared:
  doc.EnableWorksharing('99_LEVELS AND GRIDS','30_INTERIOR')

#Get the Workset Table
wst = doc.GetWorksetTable()

# Make sure that each of the newWorksets are unique
# and create them
for aWorkset in newWorksets:
  #Make sure that the work doesn't already exist
  if wst.IsWorksetNameUnique(doc,aWorkset):
    try:
      tranny = Transaction(doc)
      tranny.Start('Creating Workset ' + aWorkset)
      #Create the Workset
      Workset.Create(doc,aWorkset)
      tranny.Commit()
    except Exception  as e:
      print e.message
      tranny.RollBack()
      tranny.Dispose()
  else:
    print aWorkset + 'Already Exists'

#Save the Document  
doc.Save()

ShowDone()
