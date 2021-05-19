"""
:author Basker12
"""
import shutil
try:
    from tkinter import *
except ImportError:
    from tkinter import *
from tkinter import filedialog
import os
import csv
from tkinter import messagebox
from csv import writer
import pygame
import pandas as pd
from musicSettings import Music

root = Tk()
root.title('Add a new Pokemon')

iconFile = PhotoImage(file='formating/ball.png')
root.iconphoto(False, iconFile) # Icon Image

HEIGHT = 642
WIDTH = 405
root.geometry(f"{HEIGHT}x{WIDTH}")

root.minsize(WIDTH, HEIGHT)
root.maxsize(WIDTH, HEIGHT)

background = PhotoImage(file='formating/newpkbg.png')

Canvas = Canvas(root, width=WIDTH, height=HEIGHT, highlightbackground='#9C9FA5', highlightthickness='4')
Canvas.pack(fill='both', expand='True')
Canvas.create_image(0, 0, image=background,
                    anchor='nw')

newPokeName = Entry(root, font=('times', 8, 'bold'), borderwidth='4',
                    bg='#9C9FA5',
                    fg='#5778BB')

newPokeName.place(relx=0.02, rely=0.105,
                  relheight=0.09, relwidth=0.38)

newPokeName.insert(0, f"Your new Pokemon's name")

pokemonTypes = {'None': 1, 'Water': 2, 'Fire': 3, 'Poison': 4, # Pokemon types dictionary
                 'Grass': 5, 'Ground': 6, 'Normal': 7, 'Bug': 8,
                 'Electric': 9, 'Fairy': 10, 'Fighting': 11, 'Psychic': 12,
                 'Rock': 13, 'Ghost': 14, 'Ice': 15, 'Dragon': 16,
                 'Dark': 17, 'Steel': 18}

var1 = StringVar(root)
var1.set('Type 1')

newType1 = OptionMenu(root, var1, *pokemonTypes)
newType1.config(bg='#9C9FA5', fg='#5778BB', borderwidth='4')
newType1["menu"].config(bg='#9C9FA5', fg='#5778BB', font=('times', 8, 'bold'))

newType1.place(relx=0.60, rely=0.105,
               relheight=0.09, relwidth=0.38)

var2 = StringVar(root)
var2.set('Type 2')

newType2 = OptionMenu(root, var2, *pokemonTypes)
newType2.config(bg='#9C9FA5', fg='#5778BB', borderwidth='4')
newType2["menu"].config(bg='#9C9FA5', fg='#5778BB', font=('times', 8, 'bold'))

newType2.place(relx=0.02, rely=0.210,
               relheight=0.09, relwidth=0.38)

newGen = Entry(root, font=('times', 8, 'bold'), borderwidth='4',
               bg='#9C9FA5',
               fg='#5778BB')

newGen.place(relx=0.60, rely=0.210,
             relheight=0.09, relwidth=0.38)

newGen.insert(0, f"Pokemon's Generation")

var = StringVar(root)
var.set('Legendary')

legendaryOption = OptionMenu(root, var, 'True', 'False') # Creates a drop down menu
legendaryOption.config(bg='#9C9FA5', fg='#5778BB', borderwidth='4') # The colour of the menu
legendaryOption["menu"].config(bg='#9C9FA5', fg='#5788BB', font=('times', 15, 'bold')) # The colour of the drop down


legendaryOption.place(relx=0.30, rely=0.630,
                      relheight=0.09, relwidth=0.38)

newAttack = Entry(root, font=('times', 8, 'bold'), borderwidth='4',
                  bg='#9C9FA5',
                  fg='#5778BB')

newAttack.insert(0, f"Pokemon's attack stat")

newAttack.place(relx=0.02, rely=0.315,
                relheight=0.09, relwidth=0.38)

newHP = Entry(root, font=('times', 8, 'bold'), borderwidth='4',
              bg='#9C9FA5',
              fg='#5778BB')

newHP.insert(0, f"Pokemon's HP")

newHP.place(relx=0.60, rely=0.315,
            relheight=0.09, relwidth=0.38)

newDefence = Entry(root, font=('times', 8, 'bold'), borderwidth='4',
                   bg='#9C9FA5',
                   fg='#5778BB')

newDefence.insert(0, f"Pokemon's defence stat")

newDefence.place(relx=0.02, rely=0.420,
                 relheight=0.09, relwidth=0.38)

newSpecialAttack = Entry(root, font=('times', 8, 'bold'), borderwidth='4',
                       bg='#9C9FA5',
                       fg='#5778BB')

newSpecialAttack.insert(0, f"Pokemon's special attack")

newSpecialAttack.place(relx=0.60, rely=0.420,
                     relheight=0.09, relwidth=0.38)

newSpecialDefence = Entry(root, font=('times', 8, 'bold'), borderwidth='4',
                       bg='#9C9FA5',
                       fg='#5778BB')

newSpecialDefence.insert(0, f"Pokemon's special defence")

newSpecialDefence.place(relx=0.60, rely=0.525,
                     relheight=0.09, relwidth=0.38)

newSpeed = Entry(root, font=('times', 8, 'bold'), borderwidth='4',
                 bg='#9C9FA5',
                 fg='#5778BB')

newSpeed.insert(0, f"Pokemon's Speed")

newSpeed.place(relx=0.02, rely=0.525,
               relheight=0.09, relwidth=0.38)

createButton = Button(root, text='CREATE POKEMON', font=('times', 12, 'bold'), borderwidth='4',
                     bg='#9C9FA5',
                     fg='#5778BB',
                     width='15',
                      command=lambda: createdPokemon())

createButton.place(relx=0.25, rely=0.750,
                   relheight=0.09, relwidth=0.5)

homeButton = Button(root, text='HOME', font=('times', 12, 'bold'), borderwidth='4',
                    bg='#9C9FA5',
                    fg='#5788BB',
                    width=15,
                    command=lambda: home())

homeButton.place(relx=0.35, rely=0.900,
                 relheight=0.06, relwidth=0.3)

evolutionButton = Button(root, text='Config Evo', font=('times', 12, 'bold'), borderwidth='4',
                     bg='#9C9FA5',
                     fg='#5778BB',
                     width=15,
                     command=lambda: evolution())

evolutionButton.place(relx=0.66, rely=0.900,
                      relheight=0.06, relwidth=0.3)

resetButton = Button(root, text='RESET', font=('times', 12, 'bold'), borderwidth='4',
                    bg='#9C9FA5',
                    fg='#5778BB',
                    width=15,
                    command=lambda: reset())

resetButton.place(relx=0.04, rely=0.900,
                  relheight=0.06, relwidth=0.3)

def clearText(e): # This definition clears the entry box text, instead having to do it manually
    if newPokeName.get() == "Your new Pokemon's name":
        newPokeName.delete(0, END)

def clearTextG(e):
    if newGen.get() == "Pokemon's Generation":
        newGen.delete(0, END)

def clearTextSPEED(e):
    if newSpeed.get() == "Pokemon's Speed":
        newSpeed.delete(0, END)

def clearTextAT(e):
    if newAttack.get() == "Pokemon's attack stat":
        newAttack.delete(0, END)

def clearTextDEF(e):
    if newDefence.get() == "Pokemon's defence stat":
        newDefence.delete(0, END)

def clearTextSAT(e):
    if newSpecialAttack.get() == "Pokemon's special attack":
        newSpecialAttack.delete(0, END)

def clearTextSDEF(e):
    if newSpecialDefence.get() == "Pokemon's special defence":
        newSpecialDefence.delete(0, END)

def clearTextHP(e):
    if newHP.get() == "Pokemon's HP":
        newHP.delete(0, END)

def evolution():
    pygame.mixer.music.stop()
    root.destroy()
    os.system('Python EvolutionConfig.py')

def home():
    pygame.mixer.music.stop()
    root.destroy()
    os.system("Python menu.py")

def reset():
    newPokeName.delete(0, END)
    newPokeName.insert(0, f"Your new Pokemon's name")
    var.set("Legendary")
    var1.set("Type 1")
    var2.set("Type 2")
    newHP.delete(0, END)
    newHP.insert(0, f"Pokemon's HP")
    newGen.delete(0, END)
    newGen.insert(0, f"Pokemon's Generation")
    newAttack.delete(0, END)
    newAttack.insert(0, f"Pokemon's attack stat")
    newDefence.delete(0, END)
    newDefence.insert(0, f"Pokemon's defence stat")
    newSpecialAttack.delete(0, END)
    newSpecialAttack.insert(0, f"Pokemon's special attack")
    newSpecialDefence.delete(0, END)
    newSpecialDefence.insert(0, f"Pokemon's special defence")
    newSpeed.delete(0, END)
    newSpeed.insert(0, f"Pokemon's Speed")


def createdPokemon():
    name = None

    type1 = None

    type2 = None

    hp = None

    speed = None

    attack = None

    defence = None

    specialAttack = None

    specialDefence = None

    gen = None

    df = pd.read_csv('Pokemon.csv')
    getLastID = df.iloc[-1, 0] # This finds the last element and its id (#)
    id = getLastID + 1 # This adds 1 to the id whenever a new pokemon is created

    pokename = str(newPokeName.get()) # Added str so that you're only able to input letters and not numbers
    if pokename == pokename:
        name = pokename.title()

    poketype1 = str(var1.get())
    if poketype1 == poketype1:
        type1 = poketype1.title()

    poketype2 = str(var2.get())
    if poketype2 == poketype2:
        type2 = poketype2.title()

    pokelegendary = str(var.get())
    if pokelegendary == pokelegendary:
        legendary = pokelegendary.title()

    if type1 == "Type 1":
        type1 = "None"
    if type2 == "Type 2":
        type2 = "None"

    hp = int(newHP.get())

    speed = int(newSpeed.get())

    attack = int(newAttack.get())

    defence = int(newDefence.get())

    specialAttack = int(newSpecialAttack.get())

    specialDefence = int(newSpecialDefence.get())

    gen = int(newGen.get())

    total = hp + speed + attack + defence + specialAttack + specialDefence # This takes all the Pokemon's int stats and adds them to a total

    newPokemon = [id, name, type1, type2, total, hp, attack, defence, specialAttack, specialDefence, speed, gen, legendary]

    filename = filedialog.askopenfilename(initialdir="/",
                                          title="Select a File",
                                          filetypes=((".png files",
                                                      "*.png*"),
                                                     ("all files",
                                                      "*.*")))

    shutil.copy(filename,
                f"Pokemon Pictures//{pokename}.png")
    with open('Pokemon.csv', 'a', newline='\n') as pk:  # Opens Pokemon.csv and the writes into the csv file a new pokemon
        Pokemon = writer(pk)
        Pokemon.writerow(newPokemon)
        pk.close()

    creationFeedback(name, type1, type2, hp, speed, defence, attack, specialDefence, specialAttack, gen)

def creationFeedback(name, type1, type2, hp, speed, defence, attack, specialDefence, specialAttack, gen):
    messagebox.showinfo(                    # Creates an messagebox which shoes all the pokemons stats
        "Your Pokemon was created!",
        (
            f"Your Pokemon's name is: {name}\n"
            f"It's First type is: {type1}\n"
            f"It's Second type is: {type2}\n"
            f"The Pokemon's HP is: {hp}\n"
            f"The Pokemon's speed is: {speed}\n"
            f"The Pokemon's attack is: {attack}\n"
            f"The Pokemon's defence is: {defence}\n"
            f"The Pokemon's special attack is: {specialAttack}\n"
            f"The Pokemon's special defence is: {specialDefence}\n"
            f"And Lastly the Pokemon's gen is: {gen}"

        )
    )
# clearText and its other version clears the text in an entry box
newPokeName.bind('<Button-1>', clearText)
newGen.bind('<Button-1>', clearTextG)
newSpeed.bind('<Button-1>', clearTextSPEED)
newAttack.bind('<Button-1>', clearTextAT)
newDefence.bind('<Button-1>', clearTextDEF)
newSpecialAttack.bind('<Button-1>', clearTextSAT)
newSpecialDefence.bind('<Button-1>', clearTextSDEF)
newHP.bind('<Button-1>', clearTextHP)

Music().musicPlay() # Calls the class in musicSettings and runs it
Music().musicControls(root)

# HEX Colours: #9C9FA5 - Grey | #5778BB - Blue | #DFE2EA - white
root.mainloop()
