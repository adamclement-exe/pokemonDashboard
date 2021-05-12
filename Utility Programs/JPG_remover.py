import os
from PIL import Image  # Python Image Library - Image Processing
import glob

for file in glob.glob("*.jpg"):
    os.remove(file)