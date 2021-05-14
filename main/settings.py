"""
:author Basker12
"""
try:
    from Tkinter import *
except ImportError:
    from tkinter import *
import os
import pygame

root = Tk()
root.title('Settings')

HEIGHT = 475
WIDTH = 475
root.geometry(f'{WIDTH}x{HEIGHT}')

root.minsize(WIDTH, HEIGHT)
root.maxsize(WIDTH, HEIGHT)

iconFile = PhotoImage(file='formating/ball.png') # Icon image
root.iconphoto(False, iconFile)

backgroundImage = PhotoImage(file='formating/settingsbackgroundimage.png')

Canvas = Canvas(root, width=WIDTH, height=HEIGHT, highlightbackground='#9C9FA5', highlightthickness='4')
Canvas.pack(fill='both', expand='True')
Canvas.create_image(0, 0, image=backgroundImage,
                    anchor='nw') # Created an canvas so that text and buttons are able to show the background

menuButton = Button(root, text='MENU', font=('times', 15, 'bold'), borderwidth='4',
                    bg='#9C9FA5',
                    fg='#5778BB',
                    width='36',
                    command=lambda: mainmenu()) # Runs mainmenu and goes back to the menu

menuButton.place(relx=0.025, rely=0.790,
                  relheight=0.090, relwidth=0.95)

helpButton = Button(root, text='HELP', font=('times', 15, 'bold'), borderwidth='4',
                    bg='#9C9FA5',
                    fg='#5778BB',
                    width='36',
                    command=lambda: helpsection()) # Runs helpsection and opens a txt folder

helpButton.place(relx=0.025, rely=0.890,
                 relheight=0.090, relwidth=0.95)

createAPokemon = Button(root, text='Create a pokemon', font=('times', 15, 'bold'), borderwidth='4',
                        bg='#9C9FA5',
                        fg='#5778BB',
                        width='36',
                        command=lambda: createsection()) # Runs createsection which goes to the creation window

createAPokemon.place(relx=0.025, rely=0.690,
                     relheight=0.09, relwidth=0.95)

titleImage = PhotoImage(file='formating/settingsLogo.png')
titleImage = titleImage.zoom(2)
titleImage = titleImage.subsample(3)
Canvas.create_image(250, 94, image=titleImage)

def mainmenu():
    pygame.mixer.music.stop()
    root.destroy()
    os.system('python menu.py')

def helpsection():
    pygame.mixer.music.stop()
    root.destroy()
    os.system('python Help_Menu.py')

def createsection():
    pygame.mixer.music.stop()
    root.destroy()
    os.system('python addnewpokemon.py')

# HEX Colours: #9C9FA5 - Grey | #5778BB - Blue | #DFE2EA - white
root.mainloop()
