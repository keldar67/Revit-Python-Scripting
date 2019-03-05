﻿#========================================================================#
#      _____               __                            
#      \_   \__ _ _ __     \ \  __ _ _ __ ___   ___  ___ 
#       / /\/ _` | '_ \     \ \/ _` | '_ ` _ \ / _ \/ __|
#    /\/ /_| (_| | | | | /\_/ / (_| | | | | | |  __/\__ \
#    \____/ \__,_|_| |_| \___/ \__,_|_| |_| |_|\___||___/
#
#
#  The Script looks for inserted image files and if it can find the file 
#  on disk it will tell you how big the file is in MB
#
#  February 2019
#
#========================================================================#
import os
MB = 1050625.0 #<--- Conversion bytes to MB (1024 x 1024)

#Grab the images in the model
theImages = (
  FilteredElementCollector(doc)
  .OfCategory(BuiltInCategory.OST_RasterImages)
  .OrderBy(lambda i: Element.Name.GetValue(i))
  )
  
for anImage in theImages:
  #Initialise the size at zero
  theSize = 0
  try:
    #if you find the file on disk grab the path and then the size
    thePath = anImage.Path
    theSize = round(os.path.getsize(thePath) / MB,3)
  except:
    thePath = 'Not Found'
    pass
  #Grab the image Name  
  theName = Element.Name.GetValue(anImage)
  
  #Print to screen
  print theName + ' - ' + str(theSize)