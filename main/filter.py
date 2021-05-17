"""
:author FSNCryo
"""
try:
    from Tkinter import *
except ImportError:
    from tkinter import *
import time
import os
import pygame
from musicSettings import Music

searches = open("searches.txt", "w")
searches.write('')
searches.close()
from main.__init__ import run

root = Tk()
root.title('Pokemon Index Finder')

HEIGHT = 642
WIDTH = 405

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

                  font=65, borderwidth=5)

poke_name.place(relx=0.1, rely=0.105,
                relwidth=0.40, relheight=0.07)

poke_name.insert(0, f'Name Search')

name_search_button = Button(InnerFrame,
                            bg='#dfe2ea',
                            fg='black',
                            font=('times', 11, 'bold'), borderwidth=4,
                            command=lambda: name_search(
                                poke_name.get()
                            )  # runs when Search button is clicked

                            )

name_search_button.place(relx=0.55, rely=0.105,
                         relwidth=0.35, relheight=0.07)

name_search_button["text"] = f'Search'

type1_var = StringVar(root)

type1_choices = {'Type 1': 1, 'Water': 2, 'Fire': 3, 'Poison': 4,  # Numbers Give the Types an Order
                 'Grass': 5, 'Ground': 6, 'Normal': 7, 'Bug': 8,
                 'Electric': 9, 'Fairy': 10, 'Fighting': 11, 'Psychic': 12,
                 'Rock': 13, 'Ghost': 14, 'Ice': 15, 'Dragon': 16,
                 'Dark': 17, 'Steel': 18}  # Items in Drop Down menu

type1_var.set('Type 1')  # sets Starting Value for Drop Down menu

type1_menu = OptionMenu(InnerFrame, type1_var, *type1_choices)

type1_menu.config(bg='#dfe2ea', fg='black')  # menu Icon colours

type1_menu["menu"].config(bg='#5778bb', fg='#dfe2ea')  # menu drop down colours

type1_menu.place(relx=0.1, rely=0.405,
                 relwidth=0.35, relheight=0.06)

type2_var = StringVar(root)

type2_choices = {'Type 2': 1, 'None': 2, 'Water': 3, 'Fire': 4,  # Numbers Give the Types an Order
                 'Poison': 5, 'Grass': 6, 'Ground': 7, 'Flying': 8,
                 'Electric': 9, 'Fairy': 10, 'Fighting': 11, 'Psychic': 12,
                 'Rock': 13, 'Ghost': 14, 'Ice': 15, 'Dragon': 16,
                 'Dark': 17, 'Steel': 18}  # Items in Drop Down menu

type2_var.set('Type 2')  # sets Starting Value for Drop Down menu

type2_menu = OptionMenu(InnerFrame, type2_var, *type2_choices)

type2_menu.config(bg='#dfe2ea', fg='black')  # menu Icon colours

type2_menu["menu"].config(bg='#5778bb', fg='#dfe2ea')  # menu drop down colours

type2_menu.place(relx=0.55, rely=0.405,
                 relwidth=0.35, relheight=0.06)

gen_var = StringVar(root)

gen_choices = {'Generation': 1,
               '1': 2, '2': 3, '3': 4,  # Numbers Give the Types an Order
               '4': 5, '5': 6, '6': 7}  # Items in Drop Down menu

gen_var.set('Generation')  # sets Starting Value for Drop Down menu

gen_menu = OptionMenu(InnerFrame, gen_var, *gen_choices)

gen_menu.config(bg='#dfe2ea', fg='black')  # menu Icon colours

gen_menu["menu"].config(bg='#5778bb', fg='#dfe2ea')  # menu drop down colours

gen_menu.place(relx=0.1, rely=0.545,
               relwidth=0.35, relheight=0.06)

Legendary_var = StringVar(root)

Legendary_choices = {'Legendary': 1,
                     'True': 2, 'False': 3}  # Items in Drop Down menu

Legendary_var.set('Legendary')  # sets Starting Value for Drop Down menu

Legendary_menu = OptionMenu(InnerFrame, Legendary_var, *Legendary_choices)

Legendary_menu.config(bg='#dfe2ea', fg='black')  # menu Icon colours

Legendary_menu["menu"].config(bg='#5778bb', fg='#dfe2ea')  # menu drop down colours

Legendary_menu.place(relx=0.55, rely=0.545,
                     relwidth=0.35, relheight=0.06)

stats_var = StringVar(root)

stats_choices = {'Sort': 1, 'Alphabetical': 2,
                 'HP': 3, 'Attack': 4, 'Defense': 5,  # Numbers Give the Types an Order
                 'Sp. Atk': 6, 'Sp. Def': 7, 'Speed': 8,
                 'Total': 9, 'ID': 10}  # Items in Drop Down menu

stats_var.set('Sort')  # sets Starting Value for Drop Down menu

stats_menu = OptionMenu(InnerFrame, stats_var, *stats_choices)

stats_menu.config(bg='#dfe2ea', fg='black')  # menu Icon colours

stats_menu["menu"].config(bg='#5778bb', fg='#dfe2ea')  # menu drop down colours

stats_menu.place(relx=0.1, rely=0.685,
                 relwidth=0.35, relheight=0.06)

AorD_var = StringVar(root)

AorD_choices = {'Sort Method': 1,  # Items in Drop Down menu
                'Ascending': 2, 'Descending': 3}

AorD_var.set('Sort Method')  # sets Starting Value for Drop Down menu

AorD_menu = OptionMenu(InnerFrame, AorD_var, *AorD_choices)

AorD_menu.config(bg='#dfe2ea', fg='black')  # menu Icon colours

AorD_menu["menu"].config(bg='#5778bb', fg='#dfe2ea')  # menu drop down colours

AorD_menu.place(relx=0.55, rely=0.685,
                relwidth=0.35, relheight=0.06)

Pokemon_Browser = Label(root,

                        bg='#9c9fa5', fg='#dfe2ea',

                        font=('times', 11, 'bold'))

Pokemon_Browser.place(relx=0.17, rely=0,
                      relwidth=0.66, relheight=0.09)

Pokemon_Browser["text"] = f'Pokemon Browser'  # title

help_button = Button(ButtonFrame,
                     bg='#dfe2ea',
                     fg='black',
                     font=('times', 11, 'bold'), borderwidth=4,
                     command=lambda: help())  # runs when help button is clicked

help_button.place(relx=0.66, rely=0.3,
                  relheight=0.4, relwidth=0.30)

help_button["text"] = f'Help'

search_button = Button(InnerFrame,
                       bg='#dfe2ea',
                       fg='black',
                       font=('times', 11, 'bold'), borderwidth=4,
                       command=lambda: search(
                           type1_var.get(),
                           type2_var.get(),
                           gen_var.get(),
                           Legendary_var.get(),
                           stats_var.get(),
                           AorD_var.get()
                       )  # runs when Search button is clicked

                       )

search_button.place(relx=0.55, rely=0.825,
                    relheight=0.06, relwidth=0.35)

search_button["text"] = f'Search'

view_all_button = Button(ButtonFrame,
                         bg='#dfe2ea',
                         fg='black',
                         font=('times', 11, 'bold'), borderwidth=4,
                         command=lambda: view_all())  # runs when View All button is clicked

view_all_button.place(relx=0.03, rely=0.3,
                      relheight=0.4, relwidth=0.30)

view_all_button["text"] = f'View All'

home_button = Button(ButtonFrame,
                     bg='#dfe2ea',
                     fg='black',
                     font=('times', 11, 'bold'), borderwidth=4,
                     command=lambda: home())  # runs when Home button is clicked

home_button.place(relx=0.345, rely=0.3,
                  relheight=0.4, relwidth=0.30)

home_button["text"] = f'Home'
reset_button = Button(InnerFrame,
                      bg='#dfe2ea',
                      fg='black',
                      font=('times', 11, 'bold'), borderwidth=4,
                      command=lambda: reset())  # runs when help button is clicked

reset_button.place(relx=0.1, rely=0.825,
                   relheight=0.06, relwidth=0.35)

reset_button["text"] = f'Reset'


def help():
    pygame.mixer.music.stop()
    root.destroy()
    os.system('Python Help_Menu.py')


def home():
    pygame.mixer.music.stop()
    root.destroy()
    os.system('python menu.py')


def name_search(poke_name, self=None):
    if poke_name == 'Name Search':
        return
    else:
        searches = open("pokemon data.txt", "w")
        searches.write(f"{str(poke_name)},")
        searches.close()
        root.destroy()
        run.name_search(self)


def search(type1_var, type2_var,
           gen_var, Legendary_var,
           stats_var, AorD_var,
           self=None):
    check = [type1_var, type2_var,
             gen_var, Legendary_var,
             stats_var, AorD_var]

    check_str = ['type1_var', 'type2_var',
                 'gen_var', 'Legendary_var',
                 'stats_var', 'AorD_var']

    searches = open("searches.txt", "w")
    num = 0
    for var in check:
        i = check_str[num]
        num += 1

        if var == 'Type 1':
            var = 'All'
            searches.write(str(var))
            searches.write((","))
            continue
        elif var == 'Type 2' and 'None':
            var = 'All'
            searches.write(str(var))
            searches.write((","))
            continue
        elif var == 'Generation':
            var = 'All'
            searches.write(str(var))
            searches.write((","))
            continue
        elif var == 'Legendary':
            var = "All"
            searches.write(str(var))
            searches.write((","))
            continue
        elif var == 'Sort Method':
            var = True
            searches.write(str(var))
            searches.write((","))
            continue
        elif var == 'Sort':
            var = 'id'
            searches.write(str(var))
            searches.write((","))
            continue
        elif var == 'ID':
            var = 'id'
            searches.write(str(var))
            searches.write((","))
            continue
        elif var == "Ascending":
            var = True
            searches.write(str(var))
            searches.write((","))
            continue
        elif var == "Descending":
            var = False
            searches.write(str(var))
            searches.write((","))
            continue
        elif var == "False":
            var = False
            searches.write(str(var))
            searches.write((","))
            continue
        elif var == "True":
            var = True
            searches.write(str(var))
            searches.write((","))
            continue
        else:
            if str(i) == 'gen_var':
                searches.write(str(var))
                searches.write((","))
                continue
            else:
                searches.write(str(var))
                searches.write((","))
                continue
    searches.close()
    root.destroy()

    run.refract_search(self)


def view_all(self=None):
    pygame.mixer.music.stop()
    searches = open("searches.txt", "w")
    searches.write('All,All,All,All,id,True,')
    searches.close()
    root.destroy()
    run.refract_search(self)

def reset():
    AorD_var.set('Sort')
    stats_var.set('Stats')
    Legendary_var.set('Legendary')
    gen_var.set('Generation')
    type2_var.set('Type 2')
    type1_var.set('Type 1')
    poke_name.delete(0, 'end')
    poke_name.insert(0, 'Name Search')  # resets all to default values
    searches = open("searches.txt", "w")
    searches.close()


def clearTextSearch(e):
    if poke_name.get() == 'Name Search':
        poke_name.delete(0, END)


poke_name.bind('<Button-1>', clearTextSearch)

Music().musicPlay()
Music().musicControls(root)
root.mainloop()
