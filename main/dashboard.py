"""
dev: Theo
date: 28/04/21
"""

try:
    from Tkinter import *
    import PIL.Image
    import PIL.ImageTk
except ImportError:
    from tkinter import *
    import PIL.Image
    import PIL.ImageTk
import os
import csv
# Importing Image class from PIL module
from PIL import ImageTk, Image

global count, r_val
count = 0
r_val = {}

root = Tk()

HEIGHT = 642
WIDTH = 405

root.minsize(WIDTH, HEIGHT)
root.maxsize(WIDTH, HEIGHT)
root.title("Pokemon Index Finder")
iconFile = PhotoImage(file="formating/ball.png")  # Icon image
root.iconphoto(False, iconFile)

canvas = Canvas(root, height=HEIGHT, width=WIDTH, bg="#9C9FA5", highlightbackground="black", highlightthickness=2)
canvas.pack()

type1PicFile = PhotoImage(file="pokemonTypes/Icon_Ice.png")  # change image with the filtered type from csv
canvas.create_image(0, 100, image=type1PicFile)

# needs a if type2 exists function here when implementing

type2PicFile = PhotoImage(file="pokemonTypes/Icon_Ice.png")  # change image with the filtered type from csv
canvas.create_image(0, 100, image=type2PicFile)

frame = Frame(canvas,
              bg="#5778BB", highlightbackground="black", highlightthickness=5)

frame.place(relx=0.5, rely=0.10,
            width=385, height=472,
            anchor="n")

bottomBar = Frame(root,
                  bg="#DFE2EA", highlightbackground="black", highlightthickness=1)  # Adds Background Shape

bottomBar.place(relx=0.5, rely=0.85,
                width=WIDTH - 10, height=86,
                anchor="n")

legendFrame = Frame(root,
                    bg="#D4AF37", highlightbackground="black", highlightthickness=0)

legendFrame.place(relx=0.5, rely=0.18,
                  relheight=0.37, relwidth=0.88,
                  anchor="n")



#if legendary == 0:
#    legendFrame.config(bg="#9C9FA5", highlightbackground="black", highlightthickness=0)

totalTitle = Label(root,
                     fg="#000000",
                     bg="#9C9FA5",
                     font=("times", 16, "bold"))

totalTitle.place(relx=0.08, rely=0.01,
                   width=350, height=50)


pokeName = Label(root,
                 bg="#2E4053",
                 fg="#DFE2EA",
                 font=("times", 11, "bold"))  # formatting text

pokeName.place(relx=0.06, rely=0.12,
               relwidth=0.50, relheight=0.05)

totalName = Label(root,
                  bg="#2E4053",
                  fg="#DFE2EA",
                  font=("times", 11, "bold"))

totalName.place(relx=0.57, rely=0.12,
                relwidth=0.2, relheight=0.05)

idName = Label(root,
               bg="#2E4053",
               fg="#DFE2EA",
               font=("times", 11, "bold"))

idName.place(relx=0.78, rely=0.12,
             relwidth=0.16, relheight=0.05)

HPName = Label(root,
               bg="#2E4053",
               fg="#DFE2EA",
               font=("times", 11, "bold"))

HPName.place(relx=0.72, rely=0.65,
             relwidth=0.2, relheight=0.05)

# type1Pic.place(relx=0.5, rely=0.5,
# relheight=0.9, relwidth=0.92, anchor="center")
type1Name = Label(root,
                  bg="#2E4053",
                  fg="#DFE2EA",
                  font=("times", 11, "bold"))

type1Name.place(relx=0.08, rely=0.56,
                relwidth=0.2, relheight=0.05)

type2Name = Label(root,
                  bg="#2E4053",
                  fg="#DFE2EA",
                  font=("times", 11, "bold"))

type2Name.place(relx=0.72, rely=0.56,
                relwidth=0.2, relheight=0.05)

generationName = Label(root,
                       bg="#2E4053",
                       fg="#DFE2EA",
                       font=("times", 11, "bold"))

generationName.place(relx=0.4, rely=0.56,
                     relwidth=0.2, relheight=0.05)

attackName = Label(root,
                   bg="#2E4053",
                   fg="#DFE2EA",
                   font=("times", 11, "bold"))

attackName.place(relx=0.08, rely=0.65,
                 relwidth=0.2, relheight=0.05)

defenceName = Label(root,
                    bg="#2E4053",
                    fg="#DFE2EA",
                    font=("times", 11, "bold"))

defenceName.place(relx=0.4, rely=0.65,
                  relwidth=0.2, relheight=0.05)

spAttackName = Label(root,
                     bg="#2E4053",
                     fg="#DFE2EA",
                     font=("times", 11, "bold"))

spAttackName.place(relx=0.08, rely=0.75,
                   relwidth=0.2, relheight=0.05)

spDefenceName = Label(root,
                      bg="#2E4053",
                      fg="#DFE2EA",
                      font=("times", 11, "bold"))

spDefenceName.place(relx=0.4, rely=0.75,
                    relwidth=0.2, relheight=0.05)

speedName = Label(root,
                  bg="#2E4053",
                  fg="#DFE2EA",
                  font=("times", 11, "bold"))

speedName.place(relx=0.72, rely=0.75,
                relwidth=0.2, relheight=0.05)

# formating/imagePlace.PNG


pokemonPicFile = PhotoImage(file=f"formating/imagePlace.png")  # change image with the filtered pokemon

pokemonPicFile = pokemonPicFile.zoom(2)  # Resizes images
pokemonPicFile = pokemonPicFile.subsample(1)

pokemonPic = Label(legendFrame,
                   image=pokemonPicFile)
pokemonPic.place(relx=0.5, rely=0.5,
                 relheight=0.9, relwidth=0.92, anchor="center")

type1IconFile = PhotoImage(file="formating/PokemonTypes.PNG")  # Icon1 image    CHANGE THIS TO INDIVIDUAL TYPES
type2IconFile = PhotoImage(file="formating/PokemonTypes.PNG")  # Icon2 image

backButtonFile = PhotoImage(file="formating/Previous.PNG")  # Back Button image

back_button = Button(bottomBar,
                     bg="#DFE2EA",
                     fg="#DFE2EA",
                     image=backButtonFile,
                     font=("times", 11, "bold"), borderwidth=0,

                     command=lambda: back_button_push())  # on_button_push() Runs When a BUTTON is Pushed

back_button.place(relx=0.0, rely=0.5,
                  relheight=0.9, relwidth=0.3, anchor="w")

homeButtonFile = PhotoImage(file="formating/Home.PNG")  # home Button image

home_button = Button(bottomBar,
                     bg="#DFE2EA",
                     fg="#DFE2EA",
                     image=homeButtonFile,
                     font=("times", 11, "bold"), borderwidth=0,

                     command=lambda: home_button_push())  # on_button_push() Runs When a BUTTON is Pushed

home_button.place(relx=0.35, rely=0.5,
                  relheight=0.9, relwidth=0.3, anchor="w")

pageLabel = Button(bottomBar,
                     bg="#DFE2EA",
                     fg="black",
                     font=("times", 11, "bold"), borderwidth=0,

                     command=lambda: home_button_push())  # on_button_push() Runs When a BUTTON is Pushed

pageLabel.place(relx=0.45, rely=0.85,
                  relheight=0.25, relwidth=0.1, anchor="w")

nextButtonFile = PhotoImage(file="formating/Next.PNG")  # next Button image

next_button = Button(bottomBar,
                     bg="#DFE2EA",
                     fg="#DFE2EA",
                     image=nextButtonFile,
                     font=("times", 11, "bold"), borderwidth=0,

                     command=lambda: next_button_push())  # on_button_push() Runs When a BUTTON is Pushed

next_button.place(relx=0.7, rely=0.5,
                  relheight=0.9, relwidth=0.3, anchor="w")


def run():
    load()
    set_values()


def load():

    pokemon = "Pokemon.csv"
    name = open("searches.txt", "r")
    var = name.readline()
    name.close()
    var = (var[:-1]).split(",")
    line_count = 0
    totalPoke = 0

    with open(pokemon, 'r') as csvfile:
        pokemon = csv.reader(csvfile)
        for row in pokemon:
            row = list(row)
            if line_count != 0:
                leg = False
                if row[12] == "True":
                    leg = True

                if row[1] in var:
                    r_val[row[1]] = row
            line_count += 1

    return r_val


def set_values():

    # | Id [0] | name [1] | type1 [2] | type2 [3] | Total [4] | hp [5] | Attack [6]
    # | Defense [7] | Sp. Atk [8] | Sp. Def [9] | Speed [10] | Generation [11] | Legendary [12]
    name = list(r_val)
    name = name[count]

    idName["text"] = f"ID: {r_val[name][0]}"
    pokeName["text"] = f"{r_val[name][1]}"
    type1Name["text"] = f"{r_val[name][2]}"
    type2Name["text"] = f"{r_val[name][3]}"
    totalName["text"] = f"Total: {r_val[name][4]}"
    HPName["text"] = f"HP: {r_val[name][5]}"
    attackName["text"] = f"Atk: {r_val[name][6]}"
    defenceName["text"] = f"Def: {r_val[name][7]}"
    spAttackName["text"] = f"Sp.Atk: {r_val[name][8]}"
    spDefenceName["text"] = f"Sp.Def: {r_val[name][9]}"
    speedName["text"] = f"Speed: {r_val[name][10]}"
    generationName["text"] = f"Gen: {r_val[name][11]}"
    legendary = r_val[name][12]
    totalTitle["text"] = f"Total # of Filtered Pokemon: {len(r_val)}"
    pageLabel["text"] = f"{count+1}/{len(r_val)}"       #sets page number

    if legendary == 'False':        #Creates boolean to avoid errors
        legendary = False
    elif legendary == 'True':
        legendary = True

    #  sets picture
    legendFrame.forget()        #changes the background depending on legendary or not
    if legendary == False:
        legendFrame.config(bg="#9C9FA5", highlightbackground="black", highlightthickness=0)
    elif legendary == True:
        legendFrame.config(bg="#D4AF37", highlightbackground = "black", highlightthickness = 0)

    legendFrame.place(relx=0.5, rely=0.18,
                      relheight=0.37, relwidth=0.88,            #replaces after config
                      anchor="n")

    try:
        pokemonPicFile = PhotoImage(file=f"Pokemon Pictures/{r_val[name][1].lower()}.png")
    except:
        pokemonPicFile = PhotoImage(file=f"formating/imagePlace.png")
    pokemonPic = Label(legendFrame,
                       image=pokemonPicFile)
    pokemonPicFile = pokemonPicFile.zoom(2)  # Resizes images
    pokemonPicFile = pokemonPicFile.subsample(1)

    pokemonPic.place(relx=0.5, rely=0.5,
                     relheight=0.9, relwidth=0.92, anchor="center")


def home_button_push():
    root.destroy()
    os.system('python menu.py')


def next_button_push():
    global count, r_val
    if count != len(r_val) - 1:
        back_button.place(relx=0.0, rely=0.5,
                          relheight=0.9, relwidth=0.3, anchor="w")

        count += 1
    else:
        next_button.place_forget()

    load()
    set_values()


def back_button_push():
    global count, r_val
    if count != 0:
        next_button.place(relx=0.7, rely=0.5,
                          relheight=0.9, relwidth=0.3, anchor="w")

        count -= 1
    else:
        back_button.place_forget()

    load()
    set_values()


# HEX Colours: #9C9FA5 - Grey | #5778BB - Blue | #DFE2EA - white


run()
root.mainloop()
