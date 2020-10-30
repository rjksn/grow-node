from ndviTakeImage import TakePicture
from ndviPreProcess import PreProcess
import ndviProcess 
import os
import time
import signal

scriptDirectory = os.path.dirname(os.path.realpath(__file__))
imageDirectory = f"{scriptDirectory}/../data/images"

camera = TakePicture()
imageFilename = camera.capture(imageDirectory)

preProcess = PreProcess(imageDirectory, imageFilename)
imgResizeFilePath = preProcess.resize()

processedImgFilename = "{}/dvi-{}.png".format(imageDirectory, preProcess.timestamp)
ndviProcess.ndvi(imgResizeFilePath, processedImgFilename, processedImgFilename)

while not os.path.exists(processedImgFilename):
    time.sleep(5)

