def GetImportedCADs(document):
  return list(document.GetElements[ImportInstance]().Where(lambda i: not i.IsLinked))

# NOTE: links must be loaded if they are to be included in the report!
def ReportImportedCADs(document):
  docs = list()
  docs.append(document)
  for link in document.GetLinkedDocuments():
    docs.append(link)
  for d in docs:
    print "-" * 75
    print "Document: '" + d.Title + "'"
    print
    print "CAD Imports:"
    cads = list(GetImportedCADs(d))
    if len(cads) > 0:
      for cad in cads:
        view = d.GetElement(cad.OwnerViewId)
        print "  '" + cad.get_Parameter(BuiltInParameter.IMPORT_SYMBOL_NAME).AsString() + "'", ("'" + view.Name  + "'") if view is not None else "<NO VIEW>"
    else:
      print "  [NO CAD IMPORTS]"
    print "-" * 75
    
ReportImportedCADs(doc)