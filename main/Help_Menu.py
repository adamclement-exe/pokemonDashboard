try:
    from Tkinter import *
except ImportError:
    from tkinter import *
import os
root = Tk()
root.title('Pokemon Index Finder')

HEIGHT = 642  # 642
WIDTH = 405  # 405

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
###

poke_name = Entry(InnerFrame,

                  bg='#dfe2ea', fg='black',

                  font=70, borderwidth=5)

poke_name.place(relx=0.25, rely=0.105,
                relwidth=0.5, relheight=0.09)

poke_name.insert(0, f'Name Search')


listbox = Listbox(root)

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

###

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

home_button.place(relx=0.345, rely=0.3,
                  relheight=0.4, relwidth=0.30)

home_button["text"] = f'Home'


scrollbar = Scrollbar(InnerFrame,
                       bg='#5778bb',
                       highlightthickness=0,highlightbackground='#5778bb')

scrollbar.pack(side = RIGHT, fill = BOTH)

listbox = Listbox(InnerFrame,
                       bg='#5778bb',
                       fg='black',
                       font=('times', 11, 'bold'), highlightthickness=0,highlightbackground='#5778bb')

listbox.pack(side=LEFT,expand=True, fill=BOTH)

for i in range(100):
    listbox.insert(END, "Hello")

listbox.config(yscrollcommand=scrollbar.set)

scrollbar.config(command=listbox.yview)


def home():
    root.destroy()
    os.system('python menu.py')

root.mainloop()
