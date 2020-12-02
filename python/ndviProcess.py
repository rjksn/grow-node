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
