try:
    from Tkinter import *
except ImportError:
    from tkinter import *
from tkinter import WORD
import os
import pygame
from musicSettings import Music

root = Tk()
root.title('Pokemon Index Finder')

HEIGHT = 642  # 642
WIDTH = 405  # 405

iconFile = PhotoImage(file='formating/ball.png') # Icon image
root.iconphoto(False, iconFile)

root.minsize(WIDTH, HEIGHT)
root.maxsize(WIDTH, HEIGHT)

background = PhotoImage(file='formating/helpMenubg2.png')

canvas = Canvas(root, height=HEIGHT, width=WIDTH, highlightbackground='#9C9FA5')
canvas.pack(fill='both', expand='True')
canvas.create_image(0, 0, image=background,
                    anchor='nw')

listbox = Text(root, wrap=WORD)

listbox.pack(side=LEFT, fill=BOTH)

scrollbar = Scrollbar(root)

scrollbar.pack(side=RIGHT, fill=BOTH)

listbox.insert(END, "Hello")

# Attaching Listbox to Scrollbar
# Since we need to have a vertical
# scroll we use yscrollcommand
listbox.config(yscrollcommand=scrollbar.set)

# setting scrollbar command parameter
# to listbox.yview method its yview because
# we need to have a vertical view
scrollbar.config(command=listbox.yview)

#OuterFrame = Frame(root,
                   #bg='#9c9fa5')

#OuterFrame.place(relx=0.5, rely=0.0,
                 #relwidth=1, relheight=1,
                 #anchor='n')

InnerFrame = Frame(root,
                   bg='#F9E1DD')

InnerFrame.place(relx=0.5, rely=0.09,
                 relwidth=0.90, relheight=0.75,
                 anchor='n')

canvas.create_text(220, 28, text='Menu Help', font=('times', 20, 'bold'))

home_button = Button(root,
                     bg='#9C9FA5',
                     fg='#5778BB',
                     font=('times', 12, 'bold'), borderwidth=4,
                     command=lambda: home())  # runs when Home button is clicked

home_button.place(relx=0.11, rely=0.900,
                  relheight=0.06, relwidth=0.3)

home_button["text"] = f'HOME'

settings_button = Button(root,
                     bg='#9C9FA5',
                     fg='#5778BB',
                     font=('times', 12, 'bold'), borderwidth=4,
                     command=lambda: settings_menu())  # runs when Home button is clicked

settings_button.place(relx=0.55, rely=0.900,
                  relheight=0.06, relwidth=0.3)

settings_button["text"] = f'SETTINGS'


scrollbar = Scrollbar(InnerFrame,
                      bg='white',
                      highlightthickness=0, highlightbackground='#5778bb')

scrollbar.pack(side=RIGHT, fill=BOTH)

listbox = Text(InnerFrame,
                  wrap=WORD,
                  bg='#F9E1DD',
                  fg='black',
                  font=('times', 11, 'bold'), highlightthickness=0, highlightbackground='#5778bb')

listbox.pack(side=LEFT, expand=True, fill=BOTH)

listbox.config(yscrollcommand=scrollbar.set)

scrollbar.config(command=listbox.yview)

dev_manual_var = StringVar(root)

dev_manual_choices = {'Madmegsox1', 'FSNCryo', 'Basker12', 'Hiddenmaask', 'PointlessQuack', 'DraconicDroid',
                      'Squidnugi','Owen'}  # Items in Drop Down menu

dev_manual_var.set('Dev Manual Select')  # sets Starting Value for Drop Down menu
file = open(f"manual/Dev Manual Select.txt", "r")
lines = file.readlines()
for line in lines:
    listbox.insert(END, line)

def manual(dev_manual_var):
    listbox.delete(1.0, END)
    file = open(f"manual/{dev_manual_var}.txt", "r")
    lines = file.readlines()
    for line in lines:
        listbox.insert(END, line)
        if dev_manual_var == "FSNCryo":
            listbox.config(font=('Courier New', 11, 'bold'))
        else:
            listbox.config(font=('times', 11, 'bold'))

    #  print(dev_manual_var)


dev_manual_menu = OptionMenu(root, dev_manual_var, *dev_manual_choices, command=manual)

dev_manual_menu.config(bg='#9C9FA5', fg='#5778BB')  # menu Icon colours

dev_manual_menu["menu"].config(bg='#9C9FA5', fg='#5778BB')  # menu drop down colours

dev_manual_menu.place(relx=0.025, rely=0.025,
                      relwidth=0.35, relheight=0.04)

def home():
    pygame.mixer.music.stop()
    root.destroy()
    os.system('python menu.py')

def settings_menu():
    pygame.mixer.music.stop()
    root.destroy()
    os.system('python settings.py')

Music().musicPlay()
Music().musicControls(root)
root.mainloop()
