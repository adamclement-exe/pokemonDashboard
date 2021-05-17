"""
:author Madmegsox1
"""

from PIL import Image
from PIL import ImageFilter
import random


class GenBackground:
    def __init__(self, image, bg):
        self.img = Image.open(image).convert("RGBA")
        self.bg = Image.new("RGB", (202, 115))
        self.shadow = Image.open(bg)
        self.copy()

    def copy(self):
        self.img.thumbnail((100,100))
        for i in range(1000):
            x = random.randint(-100, 202)
            y = random.randint(-100, 115)
            copyImg = self.img.copy()
            self.bg.paste(copyImg, (x, y), copyImg)

        gaussImage = self.bg.filter(ImageFilter.GaussianBlur(1.3))
        copyBg = self.shadow.copy()
        gaussImage.paste(copyBg, (0,0), copyBg)
        gaussImage.save("bg.png")
