import clr
clr.AddReference('Microsoft.Office.Interop.Outlook')
import Microsoft.Office.Interop.Outlook as Outlook

olApp = Outlook.ApplicationClass()
from System.Runtime.InteropServices import Marshal
outlook = Marshal.GetActiveObject("Outlook.Application")

mapi = outlook.GetNamespace("MAPI")
print "Current User: " + mapi.CurrentUser.Name