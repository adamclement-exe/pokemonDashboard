try:
    from Tkinter import *
except ImportError:
    from tkinter import *

root = Tk()
root.title('Pokemon Index Finder')

HEIGHT = 642 # 642
WIDTH = 405 # 405

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

ButtonFrame = Frame(root,
                   bg='#dfe2ea')

ButtonFrame.place(relx=0.5, rely=0.87,
                 relwidth=1, relheight=0.12,
                 anchor='n')

poke_name = Entry(InnerFrame,

                  bg='#dfe2ea', fg='black',

                  font=70, borderwidth=5)

poke_name.place(relx=0.25, rely=0.105,
                relwidth=0.5, relheight=0.09)

poke_name.insert(0, f'Search')


Pokemon_Browser = Label(root,

                        bg='#9c9fa5', fg='#dfe2ea',

                        font=('times', 11, 'bold'))

Pokemon_Browser.place(relx=0.17, rely=0,
                      relwidth=0.66, relheight=0.09)

Pokemon_Browser["text"] = f'Pokemon Browser' # title


help_button = Button(ButtonFrame,
                     bg='#9c9fa5',
                     fg='#dfe2ea',
                     font=('times', 11, 'bold'), borderwidth=4,
                     command=lambda: help()) # runs when help button is clicked

help_button.place(relx=0.66, rely=0.3,
                   relheight=0.4, relwidth=0.30)

help_button["text"] = f'Help'

search_button = Button(ButtonFrame,
                     bg='#9c9fa5',
                     fg='#dfe2ea',
                     font=('times', 11, 'bold'), borderwidth=4,
                     command=lambda: search()) # runs when help button is clicked

search_button.place(relx=0.345, rely=0.3,
                   relheight=0.4, relwidth=0.30)

search_button["text"] = f'Search'


view_all_button = Button(ButtonFrame,
                     bg='#9c9fa5',
                     fg='#dfe2ea',
                     font=('times', 11, 'bold'), borderwidth=4,
                     command=lambda: view_all()) # runs when help button is clicked

view_all_button.place(relx=0.03, rely=0.3,
                   relheight=0.4, relwidth=0.30)

view_all_button["text"] = f'view all'


def help():
    return

def search():
    return

def view_all():
    return

root.mainloop()