#========================================================================#
#      _____               __                            
#      \_   \__ _ _ __     \ \  __ _ _ __ ___   ___  ___ 
#       / /\/ _` | '_ \     \ \/ _` | '_ ` _ \ / _ \/ __|
#    /\/ /_| (_| | | | | /\_/ / (_| | | | | | |  __/\__ \
#    \____/ \__,_|_| |_| \___/ \__,_|_| |_| |_|\___||___/
#
#
#  The Script loops through pre-seleted elements and shows the Tooltip 
#  info which is only accessible through Worksharing display in the UI
#  this can be a bit slow in the UI and also applies to the whole view
#  rather than just select elements
#
#  December 2018
#
#========================================================================#
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