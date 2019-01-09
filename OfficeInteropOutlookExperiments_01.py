import clr
clr.AddReference('Microsoft.Office.Interop.Outlook')
import Microsoft.Office.Interop.Outlook as Outlook

#olApp = Outlook.ApplicationClass()
from System.Runtime.InteropServices import Marshal
#outlook = Marshal.GetActiveObject("Outlook.Application")

#mapi = outlook.GetNamespace("MAPI")
#print "Current User: " + mapi.CurrentUser.Name

newemail = Marshal.GetActiveObject('Outlook.Application').CreateItem(0)
newemail.Recipients.Add('ian_james@bvn.com.au')
newemail.Subject = 'This is a test'
newemail.Body = 'This is a test email\nIt should have some text in the body'
newemail.Send()