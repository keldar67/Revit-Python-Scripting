import clr
#clr.AddReferenceToFileAndPath('C:\\windows\\assembly\\GAC_MSIL\\Microsoft.Office.Interop.Excel\\15.0.0.0__71e9bce111e9429c\\Microsoft.Office.Interop.Excel.dll')
clr.AddReference('Microsoft.Office.Interop.Excel')
import Microsoft.Office.Interop.Excel as Excel

xlApp = Excel.ApplicationClass()
xlApp.Visible = True
xlDisplayAlerts = False

from System.Runtime.InteropServices import Marshal
excel = Marshal.GetActiveObject("Excel.Application")

wb = xlApp.Workbooks.Add()
ws = wb.ActiveSheet

ws.Cells[1,2].Value2 = 'Ian'

#filename = 'C:\\Users\\ijames\\Desktop\\Metric to Imperial Conversion.xlsx'
#filename = r'C:\Users\ijames\Desktop\Metric to Imperial Conversion.xlsx'

#xlWorkbook = xlApp.Workbooks.Open(filename, 0, True, 5, "", "", True, Microsoft.Office.Interop.Excel.XlPlatform.xlWindows, "\t", False, False, 0, True, 1, 0)
