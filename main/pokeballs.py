from tkinter import *
from PIL import Image, ImageTk
import csv
import os
import pygame
from musicSettings import Music
"""
put somewhere that python doesn't like non english words
"""

def info_page(list):
    poot=Toplevel()
    poot.title("Ball Info")
    poot.geometry("550x450")
    iconFile = PhotoImage(file='formating/ball.png')
    poot.iconphoto(False, iconFile)

    Label(poot,bg="#DFE2EA",
                    fg="#DFE2EA",
                    font=("times", 11, "bold"),
                    borderwidth=0, text='Name:').place(x=1,y=1)
    name = Label(poot,bg="#DFE2EA",
                    fg="#DFE2EA",
                    font=("times", 11, "bold"),
                    borderwidth=0, text=list[0])
    name.place(x=1,y=20)
    image = images(list[1])
    label = Label(poot,bg="#DFE2EA",
                    fg="#DFE2EA",
                    font=("times", 11, "bold"),
                    borderwidth=0, image=image)
    label.image = image
    label.place(x=1,y=40)
    Label(poot,bg="#DFE2EA",
                    fg="#DFE2EA",
                    font=("times", 11, "bold"),
                    borderwidth=0, text='Gen:').place(x=1,y=130)
    gen = Label(poot,bg="#DFE2EA",
                    fg="#DFE2EA",
                    font=("times", 11, "bold"),
                    borderwidth=0, text=list[2])
    gen.place(x=1,y=150)
    Label(poot,bg="#DFE2EA",
                    fg="#DFE2EA",
                    font=("times", 11, "bold"),
                    borderwidth=0, text='Catch Rate Modifier:').place(x=1,y=170)
    Catch_rate_modifier=Label(poot,bg="#DFE2EA",
                    fg="#DFE2EA",
                    font=("times", 11, "bold"),
                    borderwidth=0, text=list[3])
    Catch_rate_modifier.place(x=1,y=190)
    if len(list[4]) != 0:
        Label(poot,bg="#DFE2EA",
                    fg="#DFE2EA",
                    font=("times", 11, "bold"),
                    borderwidth=0, text='Additional Effect:').place(x=1,y=255)
        Additional_effect = Label(poot,bg="#DFE2EA",
                    fg="#DFE2EA",
                    font=("times", 11, "bold"),
                    borderwidth=0, text=list[4])
        Additional_effect.place(x=1,y=275)
        Label(poot,bg="#DFE2EA",
                    fg="#DFE2EA",
                    font=("times", 11, "bold"),
                    borderwidth=0, text='Description').place(x=1, y=310)
        Description = Label(poot,bg="#DFE2EA",
                    fg="#DFE2EA",
                    font=("times", 11, "bold"),
                    borderwidth=0, text=list[5])
        Description.place(x=1, y=330)
    else:
        Label(poot,bg="#DFE2EA",
                    fg="#DFE2EA",
                    font=("times", 11, "bold"),
                    borderwidth=0, text='Description').place(x=1,y=255)
        Description = Label(poot,bg="#DFE2EA",
                    fg="#DFE2EA",
                    font=("times", 11, "bold"),
                    borderwidth=0, text=list[5])
        Description.place(x=1, y=275)


def images(list):
    image1 = Image.open(list)
    test = ImageTk.PhotoImage(image1)
    return test

def home():
    pygame.mixer.music.stop()
    root.destroy()
    os.system('python menu.py')


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
root.title("Ball Select")
root.minsize(300, 300)
root.maxsize(1000, 1000)
iconFile = PhotoImage(file='formating/ball.png')
root.iconphoto(False, iconFile)


Label(root, text='''Click on a Ball
for info''', font=(
'Verdana', 15)).grid(row=0,column=3)

image_list = image_grab(list)


#row 1
pokeimage=images(image_list[0])
poke = Button(root, image=pokeimage,bg="#DFE2EA",
                    fg="#DFE2EA",
                    font=("times", 11, "bold"),
                    borderwidth=0,command=lambda: info_page(list[0]))
poke.grid(row=1,column=1)
greatimage=images(image_list[1])
great = Button(root, image=greatimage,bg="#DFE2EA",
                    fg="#DFE2EA",
                    font=("times", 11, "bold"),
                    borderwidth=0,command=lambda: info_page(list[1]))
great.grid(row=1,column=2)
ultraimage=images(image_list[2])
ultra = Button(root, image=ultraimage,bg="#DFE2EA",
                    fg="#DFE2EA",
                    font=("times", 11, "bold"),
                    borderwidth=0,command=lambda: info_page(list[2]))
ultra.grid(row=1,column=3)
masterimage=images(image_list[3])
master = Button(root, image=masterimage,bg="#DFE2EA",
                    fg="#DFE2EA",
                    font=("times", 11, "bold"),
                    borderwidth=0,command=lambda: info_page(list[3]))
master.grid(row=1,column=4)
safariimage=images(image_list[4])
safari = Button(root, image=safariimage,bg="#DFE2EA",
                    fg="#DFE2EA",
                    font=("times", 11, "bold"),
                    borderwidth=0,command=lambda: info_page(list[4]))
safari.grid(row=1,column=5)

#row 2
fastimage=images(image_list[5])
fast = Button(root, image=fastimage,bg="#DFE2EA",
                    fg="#DFE2EA",
                    font=("times", 11, "bold"),
                    borderwidth=0,command=lambda: info_page(list[5]))
fast.grid(row=2,column=1)
levelimage=images(image_list[6])
level = Button(root, image=levelimage,bg="#DFE2EA",
                    fg="#DFE2EA",
                    font=("times", 11, "bold"),
                    borderwidth=0,command=lambda: info_page(list[6]))
level.grid(row=2,column=2)
lureimage=images(image_list[7])
lure = Button(root, image=lureimage,bg="#DFE2EA",
                    fg="#DFE2EA",
                    font=("times", 11, "bold"),
                    borderwidth=0,command=lambda: info_page(list[7]))
lure.grid(row=2,column=3)
heavyimage=images(image_list[8])
heavy = Button(root, image=heavyimage,bg="#DFE2EA",
                    fg="#DFE2EA",
                    font=("times", 11, "bold"),
                    borderwidth=0,command=lambda: info_page(list[8]))
heavy.grid(row=2,column=4)
loveimage=images(image_list[9])
love = Button(root, image=loveimage,bg="#DFE2EA",
                    fg="#DFE2EA",
                    font=("times", 11, "bold"),
                    borderwidth=0,command=lambda: info_page(list[9]))
love.grid(row=2,column=5)

#row 3
friendimage=images(image_list[10])
friend = Button(root, image=friendimage,bg="#DFE2EA",
                    fg="#DFE2EA",
                    font=("times", 11, "bold"),
                    borderwidth=0,command=lambda: info_page(list[10]))
friend.grid(row=3,column=1)
moonimage=images(image_list[11])
moon = Button(root, image=moonimage,bg="#DFE2EA",
                    fg="#DFE2EA",
                    font=("times", 11, "bold"),
                    borderwidth=0,command=lambda: info_page(list[11]))
moon.grid(row=3,column=2)
sportimage=images(image_list[12])
sport = Button(root, image=sportimage,bg="#DFE2EA",
                    fg="#DFE2EA",
                    font=("times", 11, "bold"),
                    borderwidth=0,command=lambda: info_page(list[12]))
sport.grid(row=3,column=3)
netimage=images(image_list[13])
net = Button(root, image=netimage,bg="#DFE2EA",
                    fg="#DFE2EA",
                    font=("times", 11, "bold"),
                    borderwidth=0,command=lambda: info_page(list[13]))
net.grid(row=3,column=4)
nestimage=images(image_list[14])
nest = Button(root, image=nestimage,bg="#DFE2EA",
                    fg="#DFE2EA",
                    font=("times", 11, "bold"),
                    borderwidth=0,command=lambda: info_page(list[14]))
nest.grid(row=3,column=5)

#row 4
repeatimage=images(image_list[15])
repeat = Button(root, image=repeatimage,bg="#DFE2EA",
                    fg="#DFE2EA",
                    font=("times", 11, "bold"),
                    borderwidth=0,command=lambda: info_page(list[15]))
repeat.grid(row=4,column=1)
timerimage=images(image_list[16])
timer = Button(root, image=timerimage,bg="#DFE2EA",
                    fg="#DFE2EA",
                    font=("times", 11, "bold"),
                    borderwidth=0,command=lambda: info_page(list[16]))
timer.grid(row=4,column=2)
luxuryimage=images(image_list[17])
luxury = Button(root, image=luxuryimage,bg="#DFE2EA",
                    fg="#DFE2EA",
                    font=("times", 11, "bold"),
                    borderwidth=0,command=lambda: info_page(list[17]))
luxury.grid(row=4,column=3)
premierimage=images(image_list[18])
premier = Button(root, image=premierimage,bg="#DFE2EA",
                    fg="#DFE2EA",
                    font=("times", 11, "bold"),
                    borderwidth=0,command=lambda: info_page(list[18]))
premier.grid(row=4,column=4)
diveimage=images(image_list[19])
dive = Button(root, image=diveimage,bg="#DFE2EA",
                    fg="#DFE2EA",
                    font=("times", 11, "bold"),
                    borderwidth=0,command=lambda: info_page(list[19]))
dive.grid(row=4,column=5)

#row 5
duskimage=images(image_list[20])
dusk = Button(root, image=duskimage,bg="#DFE2EA",
                    fg="#DFE2EA",
                    font=("times", 11, "bold"),
                    borderwidth=0,command=lambda: info_page(list[20]))
dusk.grid(row=5,column=1)
healimage=images(image_list[21])
heal = Button(root, image=healimage,bg="#DFE2EA",
                    fg="#DFE2EA",
                    font=("times", 11, "bold"),
                    borderwidth=0,command=lambda: info_page(list[21]))
heal.grid(row=5,column=2)
quickimage=images(image_list[22])
quick = Button(root, image=quickimage,bg="#DFE2EA",
                    fg="#DFE2EA",
                    font=("times", 11, "bold"),
                    borderwidth=0,command=lambda: info_page(list[22]))
quick.grid(row=5,column=3)
cherishimage=images(image_list[23])
cherish = Button(root, image=cherishimage,bg="#DFE2EA",
                    fg="#DFE2EA",
                    font=("times", 11, "bold"),
                    borderwidth=0,command=lambda: info_page(list[23]))
cherish.grid(row=5,column=4)
parkimage=images(image_list[24])
park = Button(root, image=parkimage,bg="#DFE2EA",
                    fg="#DFE2EA",
                    font=("times", 11, "bold"),
                    borderwidth=0,command=lambda: info_page(list[24]))
park.grid(row=5,column=5)


#row 6
dreamimage=images(image_list[25])
dream = Button(root, image=dreamimage,bg="#DFE2EA",
                    fg="#DFE2EA",
                    font=("times", 11, "bold"),
                    borderwidth=0,command=lambda: info_page(list[25]))
dream.grid(row=6,column=2)
beastimage=images(image_list[26])
beast = Button(root, image=beastimage,bg="#DFE2EA",
                    fg="#DFE2EA",
                    font=("times", 11, "bold"),
                    borderwidth=0,command=lambda: info_page(list[26]))
beast.grid(row=6,column=4)
homeimage = images('formating\Home.PNG')
homebutton = Button(root,
                    bg="#DFE2EA",
                    fg="#DFE2EA",
                    font=("times", 11, "bold"),
                    borderwidth=0,
                    image=homeimage,
                    command=lambda: home())
homebutton.grid(row=6,column=3)

Music().musicPlay()
Music().musicControls(root)
root.mainloop()
