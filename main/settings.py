"""
:author Basker12
"""
try:
    from Tkinter import *
except ImportError:
    from tkinter import *
import os

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
                    anchor='nw') # Created an image so that text and buttons are able to show the background

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


def mainmenu():
    root.destroy()
    os.system('python menu.py')

def helpsection():
    #print("Test")
    root.destroy()
    os.system('python Help_Menu.py')

# HEX Colours: #9C9FA5 - Grey | #5778BB - Blue | #DFE2EA - white
root.mainloop()
