print 'Checking ' + doc.Application.Documents.Size.ToString() + ' Documents'
for aDocument in doc.Application.Documents:
  try:
    cmp = aDocument.GetCloudModelPath()
    guid = cmp.GetModelGUID()
    print '[' + guid.ToString() + ']' + '\t - \t' + aDocument.Title
  except Exception as e:
    print '[' + guid.ToString() + ']' + '\t - \t' + aDocument.Title + ' - Exception: ' + e.message
    