import time
from picamera import PiCamera
from collections import namedtuple

Gains = namedtuple('Gains', ['redAWB', 'blueAWB'])

class Camera:
    camera = None
  
    def __init__(self):
        self.camera = PiCamera()
        self.camera.awb_mode = "off"
        self.camera.awb_gains = Gains(redAWB=1.75, blueAWB=0.27)
        self.camera.resolution = (1920, 1080)
        # camera.hflip = True
        # camera.vflip = True

    def capture(self, path):
        imagepath = "{}/test-AWB.png".format(path)
        # time.sleep(3)
        self.camera.capture(imagepath, "png")
        self.camera.close()
        
        return imagepath