from PIL import Image, ImageFilter
import time

class PreProcess:
    def __init__(self, imageDir, imagePath):
        self.imagePath = imagePath
        self.imageDir = imageDir

    def resize(self):
        img = Image.open(self.imagePath)
        imgResize = img.resize((800,600), Image.LANCZOS)

        self.timestamp = time.strftime("%Y-%m-%d-%H")

        imgResizePath = "{}/resized-{}.png".format(self.imageDir, self.timestamp)
        imgResize.save(imgResizePath, "png")

        return imgResizePath
