try:
    from Tkinter import *
except ImportError:
    from tkinter import *

root = Tk()
root.title('Pokemon Index Finder')

HEIGHT = 342
WIDTH = 205

root.minsize(WIDTH, HEIGHT)
root.maxsize(WIDTH, HEIGHT)

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

InnerFrame1 = Frame(root,
                   bg='#dfe2ea')

InnerFrame1.place(relx=0.5, rely=0.87,
                 relwidth=1, relheight=0.12,
                 anchor='n')

poke_name = Entry(InnerFrame,
                  bg='#dfe2ea', fg='black',
                  font=70, borderwidth=5)
poke_name.place(relx=0.25, rely=0.105,
                relwidth=0.5, relheight=0.09)
poke_name.insert(0, f'Name')

Pokemon_Browser = Label(root,

                        bg='#9c9fa5', fg='#dfe2ea',

                        font=('times', 11, 'bold'))

Pokemon_Browser.place(relx=0.17, rely=0,
                      relwidth=0.66, relheight=0.09)

Pokemon_Browser["text"] = f'Pokemon Browser'


help_button = Button(InnerFrame1,
                     bg='#9c9fa5',
                     fg='#dfe2ea',
                     font=('times', 11, 'bold'), borderwidth=4,
                     command=lambda: help())

help_button.place(relx=0.25, rely=0.3,
                   relheight=0.08, relwidth=0.50)

help_button["text"] = f'Help'

def help():
    return

root.mainloop()