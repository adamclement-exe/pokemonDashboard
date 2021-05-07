"""
:author Squidnugi
"""
import csv
try:
    from Tkinter import *
except ImportError:
    from tkinter import *
import tkinter as tk
import os

# Importing Image class from PIL module
from PIL import ImageTk,Image

def file_reader(file,choice):
    list_of_stuff = []
    types = []
    with open(file, 'r') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            #makes sure the first line is not read
            if '#' not in row:
                #changes the number valuse to int from string
                row[0] = int(row[0])
                loop = 4
                while loop <= 11:
                    row[loop] = int(row[loop])
                    loop+=1
                #changes legandary True and Flase to bool from string
                row[12] = False
                if row[12] == 'True':
                    row[12] = True
                list_of_stuff.append(row)
                #creates a list of the pokemon types
                if row[2] not in types:
                    types.append(row[2])
    #returns the pokedex if False
    if choice == False:
        return list_of_stuff
    #returns the type list of True
    elif choice == True:
        return types


def pokedex_picker(pokemon,choice):
    #gen picker
    if choice == 'Gen':
        List = []
        gen = 2
        for i in pokemon:
            if i[11] == gen:
                List.append(i)
        return List
    #type picker
    elif choice == 'Type':
        List = []
        type = 'Fire'
        for i in pokemon:
            if i[3] == type or i[4] == type:
                List.append(i)
                return List
    #Legendary picker
    elif choice == 'Legendary':
        List = []
        leg = True
        for i in pokemon:
            if i[12] == leg:
                List.append(i)
        return List
    #number picker
    elif choice == 'Num':
        List = []
        num = 100
        for i in pokemon:
            if i[0] == num:
                List.append(i)
        return List
    #name picker
    elif choice == 'Name':
        List = []
        name = 'Blastoise'
        for i in pokemon:
            if i[1] == name:
                List.append(i)
        return List

def name_filter(pokemon):
    loops = 1
    for i in pokemon:
        if i[0] == loops:
            print(i)
            loops+=1

def main():
    file = 'pokemon.csv'
    pokemon = file_reader(file,False)
    types = file_reader(file,True)
    #print(pokemon)
    #print(types)
    #gen = pokedex_picker(pokemon,'Gen')
    #print(gen)
    #name_filter(pokemon)
    return pokemon

def on_button_push():  # Run Main GUI
    print("Test")

def on_home_push():
    root.destroy()
    os.system('python menu.py')

def on_next_push():
    print("Test")

def on_back_push():
    print("Test")

if __name__ == "__main__":
    pokemon = main()

root = Tk()
root.title("Pokemon Index Finder")
iconFile = PhotoImage(file="formating/ball.png")  # Icon image
root.iconphoto(False, iconFile)

HEIGHT = 642
WIDTH = 405

canvas = Canvas(root, height=HEIGHT, width=WIDTH, bg="#9C9FA5")
canvas.pack()

frame = Frame(root,
              bg="#5778BB", highlightbackground="black", highlightthickness=5)

frame.place(relx=0.5, rely=0.10,
            width=385, height=482,
            anchor="n")

bottomBar = Frame(root,
                  bg="#DFE2EA", highlightbackground="black", highlightthickness=5)

bottomBar.place(relx=0.5, rely=0.85,
                width=405, height=86,
                anchor="n")
browserTitle = Label(root,
              fg="#000000",
              bg="#9C9FA5",
              font=("times", 30, "bold"))

browserTitle.place(relx=0.08, rely=0.01,
            width=350, height=50)

browserTitle["text"] = "Pokémon Browser"

pokeName = Label(root,
              bg="#2E4053",
              fg="#DFE2EA",
              font=("times", 11, "bold"))

pokeName.place(relx=0.06, rely=0.12,
            relwidth=0.3, relheight=0.05)

pokeName["text"] = pokemon[0][1]

totalName = Label(root,
              bg="#2E4053",
              fg="#DFE2EA",
              font=("times", 11, "bold"))

totalName.place(relx=0.4, rely=0.12,
            relwidth=0.2, relheight=0.05)

totalName["text"] = "[TOTAL]"

HPName = Label(root,
              bg="#2E4053",
              fg="#DFE2EA",
              font=("times", 11, "bold"))

HPName.place(relx=0.7, rely=0.12,
            relwidth=0.1, relheight=0.05)

HPName["text"] = "[HP]"

pokemonPicFile = PhotoImage(file="formating/imagePlace.PNG")        #change image with the filtered pokemon
pokemonPic = Label(frame,
                   image=pokemonPicFile)
pokemonPic.place(relx=0.03, rely=0.1,
                   height=225, width=353)


type1IconFile = PhotoImage(file="formating/PokemonTypes.PNG")  # Icon1 image    CHANGE THIS TO INDIVIDUAL TYPES
type2IconFile = PhotoImage(file="formating/PokemonTypes.PNG")  # Icon2 image

backButtonFile = PhotoImage(file="formating/Previous.PNG")  # Back Button image

back_button = Button(bottomBar,
                      bg="#DFE2EA",
                      fg="#DFE2EA",
                      image=backButtonFile,
                      font=("times", 11, "bold"), borderwidth=0,

                      command=lambda: on_back_push())  # on_button_push() Runs When a BUTTON is Pushed

back_button.place(relx=0.0, rely=0,
                   height=75, width=100)

homeButtonFile = PhotoImage(file="formating/Home.PNG")  # home Button image

home_button = Button(bottomBar,
                      bg="#DFE2EA",
                      fg="#DFE2EA",
                      image=homeButtonFile,
                      font=("times", 11, "bold"), borderwidth=0,

                      command=lambda: on_home_push())  # on_button_push() Runs When a BUTTON is Pushed

home_button.place(relx=0.37, rely=0.2,
                   height=40, width=100)

nextButtonFile = PhotoImage(file="formating/Next.PNG")  # next Button image

next_button = Button(bottomBar,
                      bg="#DFE2EA",
                      fg="#DFE2EA",
                      image=nextButtonFile,
                      font=("times", 11, "bold"), borderwidth=0,

                      command=lambda: on_next_push())  # on_button_push() Runs When a BUTTON is Pushed

next_button.place(relx=0.75, rely=0,
                   height=75, width=100)




# HEX Colours: #9C9FA5 - Grey | #5778BB - Blue | #DFE2EA - white

root.mainloop()


"""
if __name__ == "__main__":
    main()
"""