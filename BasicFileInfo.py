#========================================================================#
#      _____               __                            
#      \_   \__ _ _ __     \ \  __ _ _ __ ___   ___  ___ 
#       / /\/ _` | '_ \     \ \/ _` | '_ ` _ \ / _ \/ __|
#    /\/ /_| (_| | | | | /\_/ / (_| | | | | | |  __/\__ \
#    \____/ \__,_|_| |_| \___/ \__,_|_| |_| |_|\___||___/
#
#
#  1. Firstly make sure that you export a list of file paths from Kibana

#
#  2. Save the file and update the path on the next line but only the
#     bit between the single quotes make sure that you leave the r''
#     importfile = r'<--yourfilename-->'
#     better still just overwrite the file below in excel.
#
#importfile = r'\\dc2-file001\practice\InfoTech\BIM\BIMbeats\Working Files\FixingBadIDs\Revit files with bad Project IDs.xlsx'
importfile = r'P:\OH\T000002\Design\BIM\_Revit\1.0 Project Files\Project Audits\2020-08\TestPaths.xlsx'
#
#  3. Add an empty column A in front of the file paths so we can use
#     this script to push the version number into that column.
#
#  July 2020
#
#========================================================================#
import os
import clr

clr.AddReference('Microsoft.Office.Interop.Excel')
import Microsoft.Office.Interop.Excel as Excel

xlApp = Excel.ApplicationClass()
xlApp.Visible = True
xlDisplayAlerts = False

from System.Runtime.InteropServices import Marshal
excel = Marshal.GetActiveObject("Excel.Application")

#Open the Excel File
wb = xlApp.Workbooks.Open(importfile)
ws = wb.ActiveSheet

#Column & Row References
col_Version = 1
col_Path = 2
cur_Row = 2

# Loop through Excel until you get a blank row
while ws.cells[cur_Row,col_Path].Value2 > '':
  # Grab the path from the current row
  thePath = ws.cells[cur_Row,col_Path].Value2
  try:
    # Make Sure that this is a Revit Project File *.rvt
    if thePath.EndsWith('.rvt'):
      # Make Sure that the file exists
      if os.path.exists(thePath):
        # Grab the version Number
        bfi = BasicFileInfo.Extract(thePath)
        msg = bfi.Format
      else:
        msg = 'Not Found'
    else:
      if thePath.endswith('.rfa'):
        msg = 'Family'
      else:
        msg = 'Unknown'
  except Exception as e:
    #print type(e)
    print e.message
    msg = 'Oops'
    pass
  
  # Write the Version or a message to the excel    
  ws.Cells[cur_Row,col_Version].Value2 = msg
  
  print thePath
  cur_Row += 1