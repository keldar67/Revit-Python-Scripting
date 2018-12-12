if selection.Count > 0:
  for s in selection:
    #Get the Worksharing Info
    wsi = WorksharingUtils.GetWorksharingTooltipInfo(doc,s.Id)
    
    print s.Category.Name + ': ' + Element.Name.GetValue(s)
    print '[' + s.Id.ToString() + ']'
    print 'Created By      : ' + wsi.Creator
    print 'Last Changed By : ' + wsi.LastChangedBy
    print 'Owner           : ' + wsi.Owner
    print '-' * 75