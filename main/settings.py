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
#home
home_button = Button(root,
                     bg='#9C9FA5',
                     fg='#5778BB',
                     font=('times', 12, 'bold'), borderwidth=4,
                     command=lambda: mainmenu())  # runs when Home button is clicked

home_button.place(relx=0.1, rely=0.900,
                  relheight=0.075, relwidth=0.35)

home_button["text"] = f'Home'

#help
help_button = Button(root, text='Help', font=('times', 12, 'bold'), borderwidth='4',
                     bg='#9C9FA5',
                     fg='#5778BB',
                      command=lambda:helpsection())

help_button.place(relx=0.55, rely=0.900,
                   relheight=0.075, relwidth=0.35)

#button 1
button = Button(root, text='BUTTON', font=('times', 15, 'bold'), borderwidth='4',
                        bg='#9C9FA5',
                        fg='#5778BB',
                        width='36',
                        command=lambda:button())

button.place(relx=0.1, rely=0.800,
                     relheight=0.075, relwidth=0.8 )


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

def button():
    pass
    #pygame.mixer.music.stop()
    #root.destroy()
    #os.system('python FILE.py')


# HEX Colours: #9C9FA5 - Grey | #5778BB - Blue | #DFE2EA - white
root.mainloop()
