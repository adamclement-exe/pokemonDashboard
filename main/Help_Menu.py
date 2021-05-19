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

#root.minsize(WIDTH, HEIGHT)
#root.maxsize(WIDTH, HEIGHT)

canvas = Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

OuterFrame = Frame(root,
                   bg='#9c9fa5')

OuterFrame.place(relx=0.5, rely=0.0,
                 relwidth=1, relheight=1,
                 anchor='n')

InnerFrame = Frame(root,
                   bg='#5778bb')

InnerFrame.place(relx=0.5, rely=0.09,
                 relwidth=0.90, relheight=0.75,
                 anchor='n')

poke_name = Entry(InnerFrame,

                  bg='#dfe2ea', fg='black',

                  font=70, borderwidth=5)

poke_name.place(relx=0.25, rely=0.105,
                relwidth=0.5, relheight=0.09)

poke_name.insert(0, f'Name Search')

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

OuterFrame = Frame(root,
                   bg='#9c9fa5')

OuterFrame.place(relx=0.5, rely=0.0,
                 relwidth=1, relheight=1,
                 anchor='n')

InnerFrame = Frame(root,
                   bg='#5778bb')

InnerFrame.place(relx=0.5, rely=0.09,
                 relwidth=0.90, relheight=0.75,
                 anchor='n')

ButtonFrame = Frame(root,
                    bg='#dfe2ea')

ButtonFrame.place(relx=0.5, rely=0.87,
                  relwidth=1, relheight=0.12,
                  anchor='n')

Pokemon_Browser = Label(root,

                        bg='#9c9fa5', fg='#dfe2ea',

                        font=('times', 11, 'bold'))

Pokemon_Browser.place(relx=0.17, rely=0,
                      relwidth=0.66, relheight=0.09)

Pokemon_Browser["text"] = f'Help Menu'  # title

home_button = Button(ButtonFrame,
                     bg='#dfe2ea',
                     fg='black',
                     font=('times', 11, 'bold'), borderwidth=4,
                     command=lambda: home())  # runs when Home button is clicked

home_button.place(relx=0.11, rely=0.3,
                  relheight=0.4, relwidth=0.30)

home_button["text"] = f'Home'

settings_button = Button(ButtonFrame,
                     bg='#dfe2ea',
                     fg='black',
                     font=('times', 11, 'bold'), borderwidth=4,
                     command=lambda: settings_menu())  # runs when Home button is clicked

settings_button.place(relx=0.55, rely=0.3,
                  relheight=0.4, relwidth=0.30)

settings_button["text"] = f'Settings'


scrollbar = Scrollbar(InnerFrame,
                      bg='#5778bb',
                      highlightthickness=0, highlightbackground='#5778bb')

scrollbar.pack(side=RIGHT, fill=BOTH)

listbox = Listbox(InnerFrame,
                  bg='#5778bb',
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
    listbox.delete(0, END)
    file = open(f"manual/{dev_manual_var}.txt", "r")
    lines = file.readlines()
    for line in lines:
        listbox.insert(END, line)

    #  print(dev_manual_var)


dev_manual_menu = OptionMenu(root, dev_manual_var, *dev_manual_choices, command=manual)

dev_manual_menu.config(bg='#9c9fa5', fg='#5778bb')  # menu Icon colours

dev_manual_menu["menu"].config(bg='#5778bb', fg='#dfe2ea')  # menu drop down colours

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
