"""
:author Basker12
"""
try:
    from tkinter import *
except ImportError:
    from tkinter import *
import os
import csv
from tkinter import messagebox
from csv import writer
import pygame
import pandas as pd
import random

pygame.mixer.init()

playlist = list(["music/Lavender_Town.mp3", "music/Team_Skull.mp3", "music/Elite_Four.mp3",
                "music/Bede_Battle.mp3", "music/Champion_Battle.mp3", "music/Driftveil_City.mp3",
                 "music/Pokemon_Theme_Lyrics.mp3", "music/Pokemon_Theme.mp3"])

randomSong = random.choice(playlist)

pygame.mixer.music.load(randomSong)# Get the first track from the playlist
pygame.mixer.music.queue(randomSong) # Queue the 2nd song
pygame.mixer.music.play() # Play the music

root = Tk()
root.title('Add a new Pokemon')

iconFile = PhotoImage(file='formating/ball.png')
root.iconphoto(False, iconFile) # Icon Image
HEIGHT = 642
WIDTH = 405
root.geometry(f'{HEIGHT}x{WIDTH}')

root.minsize(WIDTH, HEIGHT)
root.maxsize(WIDTH, HEIGHT)

background = PhotoImage(file='formating/newpkbg.png')

Canvas = Canvas(root, width=WIDTH, height=HEIGHT, highlightbackground='#9C9FA5', highlightthickness='4')
Canvas.pack(fill='both', expand='True')
Canvas.create_image(0, 0, image=background,
                    anchor='nw')

home_button = Button(root,
                     bg='#9C9FA5',
                     fg='#5778BB',
                     font=('times', 8, 'bold'), borderwidth=4,
                     command=lambda: home())  # runs when Home button is clicked

home_button.place(relx=0.06, rely=0.900,
                  relheight=0.06, relwidth=0.3)

home_button["text"] = f'Home'

evolutionButton = Button(root, text='Config Evo', font=('times', 8, 'bold'), borderwidth='4',
                     bg='#9C9FA5',
                     fg='#5778BB',
                      command=lambda:evolution())

evolutionButton.place(relx=0.64, rely=0.900,
                   relheight=0.06, relwidth=0.3)

newPokeName = Entry(root, font=('times', 8, 'bold'), borderwidth='4',
                    bg='#9C9FA5',
                    fg='#5778BB')

newPokeName.place(relx=0.02, rely=0.105,
                  relheight=0.09, relwidth=0.38)

newPokeName.insert(0, f'Your new Pokemons name')

pokemonTypes = {'Type 1': 1, 'Water': 2, 'Fire': 3, 'Poison': 4, # Pokemon types dictionary
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

newGen.insert(0, f'Pokemons Generation')

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

newAttack.insert(0, f'Pokemons attack stat')

newAttack.place(relx=0.02, rely=0.315,
                relheight=0.09, relwidth=0.38)

newHP = Entry(root, font=('times', 8, 'bold'), borderwidth='4',
              bg='#9C9FA5',
              fg='#5778BB')

newHP.insert(0, f'Pokemons HP')

newHP.place(relx=0.60, rely=0.315,
            relheight=0.09, relwidth=0.38)

newDefence = Entry(root, font=('times', 8, 'bold'), borderwidth='4',
                   bg='#9C9FA5',
                   fg='#5778BB')

newDefence.insert(0, f'Pokemons defence stat')

newDefence.place(relx=0.02, rely=0.420,
                 relheight=0.09, relwidth=0.38)

newSpecialAttack = Entry(root, font=('times', 8, 'bold'), borderwidth='4',
                       bg='#9C9FA5',
                       fg='#5778BB')

newSpecialAttack.insert(0, f'Pokemons special attack')

newSpecialAttack.place(relx=0.60, rely=0.420,
                     relheight=0.09, relwidth=0.38)

newSpecialDefence = Entry(root, font=('times', 8, 'bold'), borderwidth='4',
                       bg='#9C9FA5',
                       fg='#5778BB')

newSpecialDefence.insert(0, f'Pokemons special defence')

newSpecialDefence.place(relx=0.60, rely=0.525,
                     relheight=0.09, relwidth=0.38)

newSpeed = Entry(root, font=('times', 8, 'bold'), borderwidth='4',
                 bg='#9C9FA5',
                 fg='#5778BB')

newSpeed.insert(0, f'Pokemons Speed')

newSpeed.place(relx=0.02, rely=0.525,
               relheight=0.09, relwidth=0.38)

createButton = Button(root, text='CREATE POKEMON', font=('times', 12, 'bold'), borderwidth='4',
                     bg='#9C9FA5',
                     fg='#5778BB',
                     width='15',
                      command=lambda:createdPokemon())

createButton.place(relx=0.25, rely=0.750,
                   relheight=0.09, relwidth=0.5)

Canvas.create_text(200, 625, text='Ctrl+S = Stops music  Ctrl+P = Pauses the music  Ctrl+U = Unpauses the music',
                   font=('times', 7, 'bold'),
                   fill='#5778BB')

def stopMusic(event): # This definition stops the music completely
    pygame.mixer.music.stop()

def pauseMusic(event): # This definition pauses the music
    pygame.mixer.music.pause()

def unpauseMusic(event): # This definition unpauses the music
    pygame.mixer.music.unpause()

def clearText(e): # This definition clears the entry box text, instead having to do it manually
    if newPokeName.get() == 'Your new Pokemons name':
        newPokeName.delete(0, END)

def clearTextG(e):
    if newGen.get() == 'Pokemons Generation':
        newGen.delete(0, END)

def clearTextSPEED(e):
    if newSpeed.get() == 'Pokemons Speed':
        newSpeed.delete(0, END)

def clearTextAT(e):
    if newAttack.get() == 'Pokemons attack stat':
        newAttack.delete(0, END)

def clearTextDEF(e):
    if newDefence.get() == 'Pokemons defence stat':
        newDefence.delete(0, END)

def clearTextSAT(e):
    if newSpecialAttack.get() == 'Pokemons special attack':
        newSpecialAttack.delete(0, END)

def clearTextSDEF(e):
    if newSpecialDefence.get() == 'Pokemons special defence':
        newSpecialDefence.delete(0, END)

def clearTextHP(e):
    if newHP.get() == 'Pokemons HP':
        newHP.delete(0, END)

def evolution():
    root.destroy()
    os.system('Python newpokemonevolutionadder.py')

def home():
    root.destroy()
    os.system('Python menu.py')

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

    hp = int(newHP.get())

    speed = int(newSpeed.get())

    attack = int(newAttack.get())

    defence = int(newDefence.get())

    specialAttack = int(newSpecialAttack.get())

    specialDefence = int(newSpecialDefence.get())

    gen = int(newGen.get())

    total = hp + speed + attack + defence + specialAttack + specialDefence # This takes all the Pokemon's int stats and adds them to a total

    newPokemon = [id, name, type1, type2, total, hp, attack, defence, specialAttack, specialDefence, speed, gen, legendary]

    with open('Pokemon.csv', 'a', newline='\n') as pk:  # Opens Pokemon.csv and the writes into the csv file a new pokemon
        Pokemon = writer(pk)
        Pokemon.writerow(newPokemon)
        pk.close()

    creationFeedback(name, type1, type2, hp, speed, defence, attack, specialDefence, specialAttack, gen)

def creationFeedback(name, type1, type2, hp, speed, defence, attack, specialDefence, specialAttack, gen):
    messagebox.showinfo(                    # Creates an messagebox which shoes all the pokemons stats
        "Your Pokemon was created!",
        (
            f'Your pokemons name is: {name}\n'
            f"It's first type is: {type1}\n"
            f"It's second type is: {type2}\n"
            f"The pokemons HP is: {hp}\n"
            f"The pokemons speed is: {speed}\n"
            f"The pokemons attack is: {attack}\n"
            f"The pokemons defence is: {defence}\n"
            f"The pokemons special attack is: {specialAttack}\n"
            f"The pokemons special defence is: {specialDefence}\n"
            f"And lastly the pokemons gen is: {gen}"

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

# Music shortcuts
root.bind('<Control_L><s>', stopMusic)
root.bind('<Control_L><p>', pauseMusic)
root.bind('<Control_L><u>', unpauseMusic)


# HEX Colours: #9C9FA5 - Grey | #5778BB - Blue | #DFE2EA - white
root.mainloop()
