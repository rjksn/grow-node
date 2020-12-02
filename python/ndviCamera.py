import time
from picamera import PiCamera

class Camera:
    camera = None
  
    def __init__(self):
        self.camera = PiCamera()
        # redAWB=2.26
        redAWB=1.75
        # blueAWB=0.74
        blueAWB=0.27

        self.camera.awb_mode = "off"
        self.camera.awb_gains = (redAWB, blueAWB)
        self.camera.resolution = (1920, 1080)
        # camera.hflip = True
        # camera.vflip = True


    def capture(self, path):
        imagepath = "{}/test-AWB.png".format(path)
        # time.sleep(3)
        self.camera.capture(imagepath, "png")
        self.camera.close()
        
        return imagepath