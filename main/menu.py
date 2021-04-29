"""
:author Basker12
:author FSNCryo
"""
try: from Tkinter import *
except ImportError: from tkinter import *
from tkinter import messagebox
import os
root = Tk()
root.title('Pokemon Index Finder')
root.geometry('500x475')

iconFile = PhotoImage(file='formating/ball.png') #Icon image
root.iconphoto(False, iconFile)

backgroundImage = PhotoImage(file='formating/background.png')
canvas = Canvas(root, width=600, height=500, highlightbackground='#9C9FA5', highlightthickness='4')
canvas.pack(fill='both', expand=True)
canvas.create_image(0, 0, image=backgroundImage, anchor='nw') #Created an image so that text and buttons are able to show the background


startButton = Button(root, text='START', font=('times', 15, 'bold'), borderwidth='4',
                     fg='#5778BB',
                     bg='#9C9FA5',
                     width='35',
                     command=lambda: on_button_push()) #This runs on_button_push and prints "Test" to the terminal
startButtonWindow = canvas.create_window(250, 400, anchor='center', window=startButton)

search_button = Button(root,
                       bg='#dfe2ea',
                       fg='black',
                       font=('times', 11, 'bold'), borderwidth=4,
                       command=lambda: dev()  # runs when Dev button is clicked

                       )

search_button.place(relx=0.02, rely=0.02,
                    relheight=0.06, relwidth=0.2)

search_button["text"] = f'Devs'

def on_button_push():
    root.destroy()
    os.system('python filter.py')

def dev():
    messagebox.showinfo\
        ("Devs", (
                'Madmegsox1\n' +
                'FSNCryo\n' +
                'Basker12\n' +
                'Hiddenmaask\n' +
                'PointlessQuack\n' +
                'DraconicDroid\n' +
                'Squidnugi\n'
                )
         )
#HEX Colours: #9C9FA5 - Grey | #5778BB - Blue | #DFE2EA - white

root.mainloop()
