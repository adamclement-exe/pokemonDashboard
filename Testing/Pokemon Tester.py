import pyautogui as pg
import subprocess
import util
import time
import csv

####add this to filter.py
"""
##temp for testing
# get screen width and height
ws = root.winfo_screenwidth() # width of the screen
hs = root.winfo_screenheight() # height of the screen
# calculate x and y coordinates for the Tk root window
x = (ws/2) - (WIDTH/2)
y = (hs/2) - (HEIGHT/2)
# set the dimensions of the screen
# and where it is placed
root.geometry('%dx%d+%d+%d' % (WIDTH, HEIGHT, x, y))
##
"""
####
subprocess.Popen("Python filter.py")

f = open("../main/Pokemon.csv", "r")
csv = list(csv.reader(f, delimiter=","))

for row in csv:
    time.sleep(2)
    print(row[1])
    pg.press("tab")
    pg.write(row[1])
    pg.moveTo(1000, 360)
    pg.click()
    subprocess.Popen("Python filter.py")
