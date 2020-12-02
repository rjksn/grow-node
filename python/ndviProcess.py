from PIL import Image
import numpy as numpy
import matplotlib
matplotlib.use('Agg')

def ndviTensorFromImage(image):
    imageChannelRed, _, imageChannelBlue, _ = image.split()
    arrR = numpy.asarray(imageChannelRed).astype('float')
    arrB = numpy.asarray(imageChannelBlue).astype('float')

    redBlueDiff = (arrR - arrB)
    redBlueSum = (arrR + arrB)

    redBlueSum[redBlueSum == 0] = 0.01
    arrNDVI = redBlueDiff/redBlueSum
    return arrNDVI



# def ndvi(image, processedImgFilename, imageOutPath):
#     img = Image.open(image)

#     imgR, _, imgB, _ = img.split()

#     arrR = numpy.asarray(imgR).astype('float')
#     arrB = numpy.asarray(imgB).astype('float')
#     redBlueDiff = (arrR - arrB)
#     redBlueSum = (arrR + arrB)

#     redBlueSum[redBlueSum == 0] = 0.01
#     arrNDVI = redBlueDiff/redBlueSum

#     fastiecm = LinearSegmentedColormap.from_list('mylist', colors) 
#     plt.imsave(imageOutPath, arrNDVI, cmap=fastiecm, vmin=-1.0, vmax=1.0)
