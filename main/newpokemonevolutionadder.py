try:
    from Tkinter import *
except ImportError:
    from tkinter import *
import os
import csv

#missing evolutions detector
evo = open("PokemonEvolutions.csv","r")
evocsv = list(csv.reader(evo, delimiter=","))
poke = open("Pokemon.csv","r")
pokecsv = list(csv.reader(poke, delimiter=","))
for row in pokecsv:
    init = False
    for row1 in evocsv:
        for i in row1:
            if i == row[1]:
                init = True

    if init == False:
        print(row[1],i)

##
#gui
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

Pokemon_Browser["text"] = f'Evolution Adder'  # title

home_button = Button(ButtonFrame,
                     bg='#dfe2ea',
                     fg='black',
                     font=('times', 11, 'bold'), borderwidth=4,
                     command=lambda: home())  # runs when Home button is clicked

home_button.place(relx=0.11, rely=0.3,
                  relheight=0.4, relwidth=0.30)

home_button["text"] = f'Home'




back_button = Button(ButtonFrame,
                     bg='#dfe2ea',
                     fg='black',
                     font=('times', 11, 'bold'), borderwidth=4,
                     command=lambda: back_menu())  # runs when Home button is clicked

back_button.place(relx=0.55, rely=0.3,
                  relheight=0.4, relwidth=0.30)

back_button["text"] = f'Back'



poke_name1 = Entry(InnerFrame,

                  bg='#dfe2ea', fg='black',

                  font=65, borderwidth=5)

poke_name1.place(relx=0.1, rely=0.105,
                relwidth=0.40, relheight=0.07)

poke_name1.insert(0, f'Name of pokemon')

poke_name2 = Entry(InnerFrame,

                  bg='#dfe2ea', fg='black',

                  font=65, borderwidth=5)

poke_name2.place(relx=0.1, rely=0.205,
                relwidth=0.40, relheight=0.07)

poke_name2.insert(0, f'Name of Evolution')

name_search_button = Button(InnerFrame,
                            bg='#dfe2ea',
                            fg='black',
                            font=('times', 11, 'bold'), borderwidth=4,
                            command=lambda: name_search(
                                poke_name.get()
                            )  # runs when Search button is clicked

                            )

name_search_button.place(relx=0.55, rely=0.205,
                         relwidth=0.35, relheight=0.07)

name_search_button["text"] = f'Add'





def home():
    root.destroy()
    os.system('python menu.py')

def back_menu():
    root.destroy()
    os.system('python addnewpokemon.py')

root.mainloop()