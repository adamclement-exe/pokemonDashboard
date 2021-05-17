import os
import glob

for file in glob.glob("*.jpg"):
    os.remove(file)