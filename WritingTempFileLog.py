import os
import os.path
import time, datetime
import subprocess as sp

def GetRevitVersionNumber():
  return uiapp.Application.VersionNumber

theversion = GetRevitVersionNumber()
theModelName = doc.Title[:doc.Title.LastIndexOf('_')]
timestamp = datetime.datetime.now().strftime("(%Y-%m-%d - %H-%M)")
thePath = r'C:\Revit_Local' + theversion + '\\' + theModelName + '_ReloadLinks_' + timestamp + '.log'

print thePath

#Open, Write to the File & Close
fp = open(thePath, 'w')
fp.write('Hello World')
fp.close()

#Then Open in Notepad.exe
NotepadCommandString = 'notepad.exe' 
logfile = thePath
sp.Popen([NotepadCommandString,logfile])