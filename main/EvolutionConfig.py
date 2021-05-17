try:
    from Tkinter import *
except ImportError:
    from tkinter import *
import os
import csv
import pandas as pd
import pygame
from musicSettings import Music

#missing evolutions detector
evo = open("PokemonEvolutions.csv","r")
evocsv = list(csv.reader(evo, delimiter=","))
poke = open("Pokemon.csv","r")
pokecsv = list(csv.reader(poke, delimiter=","))
pokecsv.remove(pokecsv[0])

for row in pokecsv:
    init = False
    for row1 in evocsv:
        for i in row1:
            if i == row[1]:
                init = True

    if init == False:
        print("Missing pokemon in evolution csv")
        print(i)

#extra evolutions detector
for row in evocsv:
    init = False
    for i in row:
        for row1 in pokecsv:
            if row1[1] == i:
                init = True

    if init == False:
        print("Extra pokemon in evolution csv")
        print(i)

#gui
root = Tk()
root.title('Pokemon Index Finder')

iconFile = PhotoImage(file='formating/ball.png')
root.iconphoto(False, iconFile) # Icon Image

HEIGHT = 250
WIDTH = 250
root.geometry(f'{HEIGHT}x{WIDTH}')

root.minsize(WIDTH, HEIGHT)
root.maxsize(WIDTH, HEIGHT)

background = PhotoImage(file='formating/newpkbg.png')

Canvas = Canvas(root, width=WIDTH, height=HEIGHT, highlightbackground='#9C9FA5', highlightthickness='4')
Canvas.pack(fill='both', expand='True')
Canvas.create_image(0, 0, image=background,
                    anchor='nw')

root.title("Evolution Adder")

home_button = Button(root,
                     bg='#9C9FA5',
                     fg='#5778BB',
                     font=('times', 12, 'bold'), borderwidth=4,
                     command=lambda: home())  # runs when Home button is clicked

home_button.place(relx=0.67, rely=0.75,
                  relheight=0.2, relwidth=0.3)

home_button["text"] = f'Home'

backButton = Button(root, text='Back', font=('times', 12, 'bold'), borderwidth='4',
                     bg='#9C9FA5',
                     fg='#5778BB',
                      command=lambda: back())

backButton.place(relx=0.04, rely=0.75,
                   relheight=0.2, relwidth=0.3)

poke_name1 = Entry(root,
                  bg='#9C9FA5', fg='#5778BB',
                  font=10, borderwidth=5)

poke_name1.place(relx=0.06, rely=0.085,
                relwidth=0.90, relheight=0.3)

poke_name1.insert(0, f'Name of pokemon')

poke_name2 = Entry(root,
                  bg='#9C9FA5', fg='#5778BB',
                  font=12, borderwidth=5)

poke_name2.place(relx=0.06, rely=0.40,
                relwidth=0.90, relheight=0.3)

poke_name2.insert(0, f'Name of Evolution')

addButton = Button(root,
                            bg='#9C9FA5',
                            fg='#5778BB',
                            font=('times', 11, 'bold'), borderwidth=4,
                            command=lambda: add())

addButton.place(relx=0.35, rely=0.75,
                relwidth=0.3, relheight=0.2)

addButton["text"] = f'Add'

def clearPokeName1(e):
    if poke_name1.get() == 'Name of pokemon':
        poke_name1.delete(0, END)

def clearPokeName2(e):
    if poke_name2.get() == 'Name of Evolution':
        poke_name2.delete(0, END)

def home():
    pygame.mixer.music.stop()
    root.destroy()
    os.system('python menu.py')

def back():
    pygame.mixer.music.stop()
    root.destroy()
    os.system('python addnewpokemon.py')

def add():
    inputValue1=poke_name1.get()
    inputValue2=poke_name2.get()
    print(inputValue1)
    print(inputValue2)

    init = False
    for row in evocsv:
        for i in row:
            if i.upper() == inputValue1.upper():
                init = True
                temp1 = row
                temp2 = i

    if init == True:
        row = temp1
        i = temp2
        print("Found in file")
        a = evocsv.index(row)
        b = row.index(i)
        print(a, b)
        print(evocsv[a][b])

        if inputValue2 in evocsv[a]:
            print("Both already added")

        elif inputValue2 != "Name of Evolution":
            with open('PokemonEvolutions.csv', mode='w', newline="") as f:
                writer = csv.writer(f, delimiter=',')
                row.append(inputValue2)
                for row2 in evocsv:
                    if evocsv.index(row2) == a:
                        writer.writerow(row)
                    else:
                        writer.writerow(row2)


        else:
            print("Please enter a Evolution")

    else:
        print("Not found. Making new row")
        with open('PokemonEvolutions.csv', mode='w', newline="") as f:
            writer = csv.writer(f, delimiter=',')
            for row2 in evocsv:
                writer.writerow(row2)
            writer.writerow((inputValue1,inputValue2))

poke_name1.bind('<Button-1>', clearPokeName1) # This clears the text after a user clicks on it
poke_name2.bind('<Button-1>', clearPokeName2)

Music().musicPlay()
Music().musicControls(root)
root.mainloop()