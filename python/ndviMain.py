import os
from ndviCamera import Camera
from ndviProcess import ndviTensorFromImage
from ndviColors import fastiecm
from PIL import Image
import time
import matplotlib.pyplot as plt


SCRIPT_PATH = os.path.dirname(os.path.realpath(__file__))
OUTPUT_PATH = f"{SCRIPT_PATH}/../data/images"
TIMESTAMP = time.strftime("-%Y-%m-%d-%H")


camera = Camera()
imageFilename = camera.capture(OUTPUT_PATH)

with Image.open(imageFilename) as image:
    resized_image = image.resize((800,600), Image.LANCZOS)

resized_image.convert('RGB').save(f"{OUTPUT_PATH}/resized{TIMESTAMP}.jpg", "JPEG")

plt.imsave(f"{OUTPUT_PATH}/ndvi{TIMESTAMP}.jpg",
        ndviTensorFromImage(resized_image), cmap=fastiecm, vmin=-1.0, vmax=1.0)

