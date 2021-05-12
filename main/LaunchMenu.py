try:
    from Tkinter import *
except ImportError:
    from tkinter import *
from tkinter import messagebox
import pygame
import os
from musicSettings import Music

root = Tk()
root.title('Launch Menu')

HEIGHT = 475
WIDTH = 475

root.geometry(f'{HEIGHT}x{WIDTH}')

root.minsize(WIDTH, HEIGHT)
root.maxsize(WIDTH, HEIGHT)

iconFile = PhotoImage(file='formating/ball.png')  # Icon image
root.iconphoto(False, iconFile)

backgroundImage = PhotoImage(file='formating/background.png')

canvas = Canvas(root, width=WIDTH, height=HEIGHT, highlightbackground='#9C9FA5', highlightthickness='4')
canvas.pack(fill='both', expand=True)
canvas.create_image(0, 0, image=backgroundImage,
                    anchor='nw')

#poke browser
pokeBrowser = Button(root, text='BROWSE POKEMON', font=('times', 15, 'bold'), borderwidth='4',
                        bg='#9C9FA5',
                        fg='#5778BB',
                        width='36',
                        command=lambda: PokeBrowser())

pokeBrowser.place(relx=0.025, rely=0.390,
                     relheight=0.09, relwidth=0.95)

#view all
viewAll = Button(root, text='VIEW ALL POKEMON', font=('times', 15, 'bold'), borderwidth='4',
                        bg='#9C9FA5',
                        fg='#5778BB',
                        width='36',
                        command=lambda: ViewAll())

viewAll.place(relx=0.025, rely=0.490,
                     relheight=0.09, relwidth=0.95)

#add new pokemon
addPokemon = Button(root, text='ADD NEW POKEMON', font=('times', 15, 'bold'), borderwidth='4',
                        bg='#9C9FA5',
                        fg='#5778BB',
                        width='36',
                        command=lambda: addPokemon())

addPokemon.place(relx=0.025, rely=0.590,
                     relheight=0.09, relwidth=0.95)

#settings
settings = Button(root, text='SETTINGS', font=('times', 15, 'bold'), borderwidth='4',
                        bg='#9C9FA5',
                        fg='#5778BB',
                        width='36',
                        command=lambda: settingsMenu())

settings.place(relx=0.025, rely=0.690,
                     relheight=0.09, relwidth=0.95)

#back
backButton = Button(root, text='HOME', font=('times', 15, 'bold'), borderwidth='4',
                    bg='#9C9FA5',
                    fg='#5778BB',
                    width='36',
                    command=lambda: back())

backButton.place(relx=0.025, rely=0.790,
                  relheight=0.090, relwidth=0.95)

#help
helpButton = Button(root, text='HELP', font=('times', 15, 'bold'), borderwidth='4',
                    bg='#9C9FA5',
                    fg='#5778BB',
                    width='36',
                    command=lambda: helpMenu())

helpButton.place(relx=0.025, rely=0.890,
                 relheight=0.090, relwidth=0.95)


titleImage = PhotoImage(file='formating/logo.png')
titleImage = titleImage.zoom(2)
titleImage = titleImage.subsample(5)
canvas.create_image(250, 94, image=titleImage)


def PokeBrowser():
    root.destroy()
    os.system('python filter.py')

def settingsMenu():
    root.destroy()
    os.system('python settings.py')

def ViewAll():
    #root.destroy()
    #os.system('python ##.py')
    pass

def back():
    root.destroy()
    os.system('python menu.py')

def helpMenu():
    root.destroy()
    os.system('python Help_Menu.py')

def addPokemon():
    root.destroy()
    os.system('python addnewpokemon.py')


Music().musicPlay()
Music().musicControls(root)
root.mainloop()
