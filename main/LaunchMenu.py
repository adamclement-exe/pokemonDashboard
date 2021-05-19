try:
    from Tkinter import *
except ImportError:
    from tkinter import *
from tkinter import messagebox
import pygame
import os
from musicSettings import Music
from main.__init__ import run

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

pokeBrowser.place(relx=0.04, rely=0.05,
                     relheight=0.075, relwidth=0.92)

#view all
viewAll = Button(root, text='VIEW ALL POKEMON', font=('times', 15, 'bold'), borderwidth='4',
                        bg='#9C9FA5',
                        fg='#5778BB',
                        width='36',
                        command=lambda: ViewAll())

viewAll.place(relx=0.04, rely=0.15,
                     relheight=0.075, relwidth=0.92)

#Pokeballs
Pokeballs = Button(root, text='POKEBALLS', font=('times', 15, 'bold'), borderwidth='4',
                        bg='#9C9FA5',
                        fg='#5778BB',
                        width='36',
                        command=lambda: pokeBalls())

Pokeballs.place(relx=0.04, rely=0.700,
                     relheight=0.075, relwidth=0.92)

#add new pokemon
addPokemon = Button(root, text='ADD NEW POKEMON', font=('times', 15, 'bold'), borderwidth='4',
                        bg='#9C9FA5',
                        fg='#5778BB',
                        width='18',
                        command=lambda: addPokemon())

addPokemon.place(relx=0.04, rely=0.800,
                     relheight=0.075, relwidth=0.92)

#settings
settings = Button(root, text='SETTINGS', font=('times', 12, 'bold'), borderwidth='4',
                        bg='#9C9FA5',
                        fg='#5778BB',
                        width='15',
                        command=lambda: settingsMenu())

settings.place(relx=0.35, rely=0.900,
                     relheight=0.06, relwidth=0.3)

#back
backButton = Button(root, text='HOME', font=('times', 12, 'bold'), borderwidth='4',
                    bg='#9C9FA5',
                    fg='#5778BB',
                    width='15',
                    command=lambda: back())

backButton.place(relx=0.04, rely=0.900,
                  relheight=0.06, relwidth=0.3)

#help
helpButton = Button(root, text='HELP', font=('times', 12, 'bold'), borderwidth='4',
                    bg='#9C9FA5',
                    fg='#5778BB',
                    width='15',
                    command=lambda: helpMenu())

helpButton.place(relx=0.66, rely=0.900,
                   relheight=0.06, relwidth=0.3)


def PokeBrowser():
    pygame.mixer.music.stop()
    root.destroy()
    os.system('python filter.py')

def settingsMenu():
    pygame.mixer.music.stop()
    root.destroy()
    os.system('python settings.py')

def ViewAll(self=None):
    pygame.mixer.music.stop()
    searches = open("searches.txt", "w")
    searches.write('All,All,All,All,id,True,')
    searches.close()
    root.destroy()
    run.refract_search(self)

def pokeBalls():
    pygame.mixer.music.stop()
    root.destroy()
    os.system('python pokeballs.py')

def back():
    pygame.mixer.music.stop()
    root.destroy()
    os.system('python menu.py')

def helpMenu():
    pygame.mixer.music.stop()
    root.destroy()
    os.system('python Help_Menu.py')

def addPokemon():
    pygame.mixer.music.stop()
    root.destroy()
    os.system('python addnewpokemon.py')

Music().musicPlay()
Music().musicControls(root)
root.mainloop()
