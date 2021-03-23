import io
outfolder = "C:\\REVIT_LOCAL2019\\TEST\\"

theImages = (
  FilteredElementCollector(doc)
  .OfCategory(BuiltInCategory.OST_RasterImages)
  .OrderBy(lambda i: Element.Name.GetValue(i))
  )

imageTypes = []
imageInstances = []


for anImage in theImages:
  if ImageType == type(anImage):
    imageTypes.Add(anImage)
    img = anImage.GetImage()
    format = img.RawFormat
    outfile = outfolder + Element.Name.GetValue(anImage)
    #fs = open(outfile, 'wb')
    with open(outfile, 'wb') as f:
      #img.Save(fs, format)
      f.write(img)
      
    f.close
  else:
    imageInstances.Add(anImage)
    
  