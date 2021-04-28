"""
:author Basker12
:author FSNCryo
"""

try: from Tkinter import *
except ImportError: from tkinter import *

root = Tk()
root.title('Pokemon Index Finder')

HEIGHT = 500
WIDTH = 600

canvas = Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

iconFile = PhotoImage(file='formating/ball.png') #Icon image
root.iconphoto(False, iconFile)

frame1 = Frame(root,
               bg='#5778BB',
               highlightbackground='#9C9FA5',
               highlightthickness='4')

frame1.place(relx=0.5, rely=0.0,
             relwidth=1, relheight=1,
             anchor='n')


text1 = Label(root,
              bg='#5778BB',
              fg='#DFE2EA',
              font=('times', 50, 'bold'))

text1.place(relx=0.5, rely=0.100,
            relwidth=0.50, relheight=0.10,
            anchor="center") #anchor makes the position of your widget move

text1["text"] = 'DEVS:'

text2 = Label(root,
              bg='#5778BB',
              fg='#DFE2EA',
              font=('times', 15, 'bold'))

text2.place(relx=0.300, rely=0.25,
            relwidth=0.40, relheight=0.45)

text2["text"] = ('Madmegsox1\n' + 'FSNCryo\n' + 'Basker 12\n' + 'Hiddenmaask\n' + 'PointlessQuack\n' + 'DraconicDroid\n' + 'Squidnugi\n')


start_button = Button(frame1,
                      bg='#9C9FA5',
                      fg='#DFE2EA',
                      font=('times', 11, 'bold'), borderwidth=4,

                      command=lambda: on_button_push()) # on_button_push() Runs When a BUTTON is Pushed


start_button.place(relx=0.25, rely=0.765,
                   relheight=0.08, relwidth=0.50)

start_button["text"] = f'START'

def on_button_push(): # Run Main GUI
    print("Test")
    
#HEX Colours: #9C9FA5 - Grey | #5778BB - Blue | #DFE2EA - white

root.mainloop()