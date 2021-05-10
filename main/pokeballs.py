from tkinter import *
from tkinter.ttk import *
import csv
import os
"""
put somewhere that python doesn't like other languages (not coding languages)
"""

def info_page(list):
    print(f"""\nname: {list[0]} 
gen: {list[2]} 
multiplier: {list[3]}
Additional effect: {list[4]}
description:
{list[5]}""")

def images(list):
    photo = PhotoImage(file=list)
    photoimage = photo.subsample(1, 1)
    return photoimage

def home():
    root.destroy()
    os.system('python menu.py')

#def info_page():
#    print('test')

def image_grab(file):
    image=[]
    for row in file:
        image.append(row[1])
    return image

list = []
with open("pokeball info.csv", "r") as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        if 'ball_name' not in row:
            list.append(row)


root=Tk()
root.title("Ball select")
root.minsize(475, 475)
root.maxsize(1000, 1000)
iconFile = PhotoImage(file='formating/ball.png')  # Icon image
root.iconphoto(False, iconFile)


Label(root, text='''Click on a Ball
     for info''', font=(
'Verdana', 15)).grid(row=0,column=3)

image_list = image_grab(list)


#row 1
pokeimage=images(image_list[0])
poke = Button(root, image=pokeimage,command=lambda: info_page(list[0]))
poke.grid(row=1,column=1)
greatimage=images(image_list[1])
great = Button(root, image=greatimage,command=lambda: info_page(list[1]))
great.grid(row=1,column=2)
ultraimage=images(image_list[2])
ultra = Button(root, image=ultraimage,command=lambda: info_page(list[2]))
ultra.grid(row=1,column=3)
masterimage=images(image_list[3])
master = Button(root, image=masterimage,command=lambda: info_page(list[3]))
master.grid(row=1,column=4)
safariimage=images(image_list[4])
safari = Button(root, image=safariimage,command=lambda: info_page(list[4]))
safari.grid(row=1,column=5)

#row 2
fastimage=images(image_list[5])
fast = Button(root, image=fastimage,command=lambda: info_page(list[5]))
fast.grid(row=2,column=1)
levelimage=images(image_list[6])
level = Button(root, image=levelimage,command=lambda: info_page(list[6]))
level.grid(row=2,column=2)
lureimage=images(image_list[7])
lure = Button(root, image=lureimage,command=lambda: info_page(list[7]))
lure.grid(row=2,column=3)
heavyimage=images(image_list[8])
heavy = Button(root, image=heavyimage,command=lambda: info_page(list[8]))
heavy.grid(row=2,column=4)
loveimage=images(image_list[9])
love = Button(root, image=loveimage,command=lambda: info_page(list[9]))
love.grid(row=2,column=5)

#row 3
friendimage=images(image_list[10])
friend = Button(root, image=friendimage,command=lambda: info_page(list[10]))
friend.grid(row=3,column=1)
moonimage=images(image_list[11])
moon = Button(root, image=moonimage,command=lambda: info_page(list[11]))
moon.grid(row=3,column=2)
sportimage=images(image_list[12])
sport = Button(root, image=sportimage,command=lambda: info_page(list[12]))
sport.grid(row=3,column=3)
netimage=images(image_list[13])
net = Button(root, image=netimage,command=lambda: info_page(list[13]))
net.grid(row=3,column=4)
nestimage=images(image_list[14])
nest = Button(root, image=nestimage,command=lambda: info_page(list[14]))
nest.grid(row=3,column=5)

#row 4
repeatimage=images(image_list[15])
repeat = Button(root, image=repeatimage,command=lambda: info_page(list[15]))
repeat.grid(row=4,column=1)
timerimage=images(image_list[16])
timer = Button(root, image=timerimage,command=lambda: info_page(list[16]))
timer.grid(row=4,column=2)
luxuryimage=images(image_list[17])
luxury = Button(root, image=luxuryimage,command=lambda: info_page(list[17]))
luxury.grid(row=4,column=3)
premierimage=images(image_list[18])
premier = Button(root, image=premierimage,command=lambda: info_page(list[18]))
premier.grid(row=4,column=4)
diveimage=images(image_list[19])
dive = Button(root, image=diveimage,command=lambda: info_page(list[19]))
dive.grid(row=4,column=5)

#row 5
duskimage=images(image_list[20])
dusk = Button(root, image=duskimage,command=lambda: info_page(list[20]))
dusk.grid(row=5,column=1)
healimage=images(image_list[21])
heal = Button(root, image=healimage,command=lambda: info_page(list[21]))
heal.grid(row=5,column=2)
quickimage=images(image_list[22])
quick = Button(root, image=quickimage,command=lambda: info_page(list[22]))
quick.grid(row=5,column=3)
cherishimage=images(image_list[23])
cherish = Button(root, image=cherishimage,command=lambda: info_page(list[23]))
cherish.grid(row=5,column=4)
parkimage=images(image_list[24])
park = Button(root, image=parkimage,command=lambda: info_page(list[24]))
park.grid(row=5,column=5)


#row 6
dreamimage=images(image_list[25])
dream = Button(root, image=dreamimage,command=lambda: info_page(list[25]))
dream.grid(row=6,column=2)
beastimage=images(image_list[26])
beast = Button(root, image=beastimage,command=lambda: info_page(list[26]))
beast.grid(row=6,column=4)
homebutton = Button(root, text='home',command=lambda: home())
homebutton.grid(row=6,column=3)

root.mainloop()
