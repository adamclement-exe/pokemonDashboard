"""
:author Basker12
:author FSNCryo
"""
try:
    from Tkinter import *
except ImportError:
    from tkinter import *
from tkinter import messagebox
import pygame
import os
from musicSettings import Music

root = Tk()
root.title('Pokemon Index Finder')

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
                    anchor='nw')  # Created an image so that text and buttons are able to show the background

startButton = Button(root, text='START', font=('times', 15, 'bold'), borderwidth='4',
                     fg='#5778BB',
                     bg='#9C9FA5',
                     width='36',
                     command=lambda: on_button_push())  # Destroys current window and runs python filter.py

#  startButtonWindow = canvas.create_window((int(HEIGHT)/2), 400, anchor='center', window=startButton)
startButton.place(relx=0.025, rely=0.790,
                  relheight=0.090, relwidth=0.95)

devButton = Button(root, text='DEVS', font=('times', 15, 'bold'), borderwidth='4',
                   fg='#5778BB',
                   bg='#9C9FA5',
                   width='18',
                   command=lambda: dev()) # runs when Dev button is clicked

#  devButtonWindow = canvas.create_window(12, 468, anchor='sw', window=devButton)
devButton.place(relx=0.025, rely=0.890,
                relheight=0.090, relwidth=0.46)

settingsButton = Button(root, text='SETTINGS', font=('times', 14, 'bold'), borderwidth='4',
                        fg='#5778BB',
                        bg='#9C9FA5',
                        width='18',
                        command=lambda: settings_menu())

#  settingsButtonWindow = canvas.create_window(245, 468, anchor='sw', window=settingsButton)
settingsButton.place(relx=0.515, rely=0.890,
                     relheight=0.090, relwidth=0.46)

titleImage = PhotoImage(file='formating/logo.png')
titleImage = titleImage.zoom(2)
titleImage = titleImage.subsample(5)
canvas.create_image(250, 94, image=titleImage)


def on_button_push():
    root.destroy()
    os.system('python filter.py')


def dev():
    messagebox.showinfo(
        "Devs", (
                'Madmegsox1\n' +
                'FSNCryo\n' +
                'Basker12\n' +
                'Hiddenmaask\n' +
                'PointlessQuack\n' +
                'DraconicDroid\n' +
                'Squidnugi'
        )
    )

def settings_menu():
    root.destroy()
    os.system('python settings.py')

# HEX Colours: #9C9FA5 - Grey | #5778BB - Blue | #DFE2EA - white

Music().musicPlay()
Music().musicControls(root)

root.mainloop()
