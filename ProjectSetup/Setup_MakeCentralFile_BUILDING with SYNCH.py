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
'00_FACADE',
'10_STRUCTURE',
'20_VERTICAL CIRCULATION',
'40_FF&E',
'51_ENTOURAGE',
'60_MASSING',
'70_SAFETY IN DESIGN',
'90_LINK_BVN_SITE',
'92_LINK_CAD_SURVEY'
]

#Collaborate the model on the Network with standard default and Grid & Levels Worksets
doc.EnableWorksharing('99_LEVELS AND GRIDS','30_INTERIOR')

#Get the Workset Table
wst = doc.GetWorksetTable()

#List for worksets we are going to create
wslist = []

#Workset Config to open the workset on creation
wsconfig = WorksetConfiguration()
  
# Make sure that each of the newWorksets are unique
# and create them
for aWorkset in newWorksets:
  #Make sure that the work doesn't already exist
  if wst.IsWorksetNameUnique(doc,aWorkset):
    try:
      tranny = Transaction(doc)
      tranny.Start('Creating Workset ' + aWorkset)
      #Create the Workset
      ws = Workset.Create(doc,aWorkset)
      tranny.Commit()
      #Add the new Workset WorksetId to the list
      wslist.Append(ws.Id)
    except Exception  as e:
      print e.message
      tranny.RollBack()
      tranny.Dispose()
  else:
    print aWorkset + 'Already Exists'

#Set the new Worksets to open
wsconfig.Open(wslist)

#Save the Document  
doc.Save()

#Synch the Document
transact = TransactWithCentralOptions()

#Relinquish User Defined Worksets.
relinqOptions = RelinquishOptions(True)
relinqOptions.UserWorksets = True

#Synch Settings including message and Compact the File.
synch = SynchronizeWithCentralOptions()
synch.Comment = 'BVN Central Model Created at ' + datetime.datetime.now().isoformat()
synch.Compact = True
synch.SaveLocalBefore = False
synch.SetRelinquishOptions(relinqOptions)

doc.SynchronizeWithCentral(transact, synch)