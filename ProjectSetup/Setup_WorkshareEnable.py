#========================================================================#
#      _____               __                            
#      \_   \__ _ _ __     \ \  __ _ _ __ ___   ___  ___ 
#       / /\/ _` | '_ \     \ \/ _` | '_ ` _ \ / _ \/ __|
#    /\/ /_| (_| | | | | /\_/ / (_| | | | | | |  __/\__ \
#    \____/ \__,_|_| |_| \___/ \__,_|_| |_| |_|\___||___/
#
#  Automation of Project Setup 
#
#  This script automates making the file workshare enabled and adding 
#  the default worksets.
#
#  November 2019
#
#========================================================================#

#------------------------------------------------------------------------#
def ShowError(message):
  td = TaskDialog('Error')
  td.MainContent = message
  
  td.Show()
#------------------------------------------------------------------------#
def EnableWorksharing():
  try:
    doc.EnableWorksharing('99_LEVELS AND GRIDS', '10_ARCHITECTURE')
  except Exception as e:
    ShowError(e.message)
#------------------------------------------------------------------------#
# Make sure that the file isn't called something like
# Project1
# Project2
# Project3
# Project4
# etc...
if (
  'Project'.Equals(doc.Title[:7]) #The project name starts with 'Project'
  and
  doc.Title[7:].isnumeric() #The bit following 'Project' is a number
  ):
  print 'This file needs a proper name rather than: ' + doc.Title
  print 'before we enable Worksharing...'
  
else:
  print 'Enabling Worksharing for your File: ' + doc.Title