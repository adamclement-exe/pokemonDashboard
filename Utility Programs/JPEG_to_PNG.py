from PIL import Image
import glob

for file in glob.glob("*.jpg"):
 im = Image.open(file)
 im.save(file.replace("jpg", "png"), quality=95)
