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
import yaml
from util import backgroundGenerator as bg
from musicSettings import Music
import pygame
import util
# Importing Image class from PIL module
from PIL import ImageTk, Image

global count, r_val
count = 0
r_val = {}
typecolour = '#5778BB'


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

frame = Frame(canvas,
              bg=typecolour, highlightbackground="black", highlightthickness=5)
#5778BB
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

# if legendary == 0:
#    legendFrame.config(bg="#9C9FA5", highlightbackground="black", highlightthickness=0)

logo = PhotoImage(file='formating/pokeBrowserLogo.png')
logo = logo.zoom(2)
logo = logo.subsample(3)
canvas.create_image(200, 35, image=logo)

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
                     font=("times", 11, "bold"), borderwidth=4,

                     command=lambda: home_button_push())  # on_button_push() Runs When a BUTTON is Pushed

home_button.place(relx=0.35, rely=0.5,
                  relheight=0.9, relwidth=0.3, anchor="w")

nextButtonFile = PhotoImage(file="formating/Next.PNG")  # next Button image

next_button = Button(bottomBar,
                     bg="#DFE2EA",
                     fg="#DFE2EA",
                     image=nextButtonFile,
                     font=("times", 11, "bold"), borderwidth=0,

                     command=lambda: next_button_push())  # on_button_push() Runs When a BUTTON is Pushed

next_button.place(relx=0.7, rely=0.5,
                  relheight=0.9, relwidth=0.3, anchor="w")

pokemonPicFile = PhotoImage(file=f"Pokemon Pictures/abra.png")
ss = PhotoImage(file=f"Pokemon Pictures/abra.png")

# pokemonPicFile = PhotoImage(file=f"formating/imagePlace.png")

pokemonPicFile = pokemonPicFile.zoom(4)  # Resizes images
pokemonPicFile = pokemonPicFile.subsample(1)

pokemonPic = Label(legendFrame,
                   image=ss, bg="#5778BB")

pokemonPic.place(relx=0.5, rely=0.5,
                 relheight=0.9, relwidth=0.92, anchor="center")

type1File = PhotoImage(file=f"pokemonTypes/Icon_None.png")

type1File = type1File.zoom(1)
type1File = type1File.subsample(3)

type1Pic = Label(legendFrame,
                 image=type1File, bg='white')  # bg="#5778BB"

type1Pic.place(relx=0.83, rely=0.11,
               relheight=0.10, relwidth=0.07, anchor="center")

type2File = PhotoImage(file=f"pokemonTypes/Icon_None.png")

type2File = type2File.zoom(1)
type2File = type2File.subsample(3)

type2Pic = Label(legendFrame,
                 image=type2File, bg="#5778BB")

type2Pic.place(relx=0.915, rely=0.11,
               relheight=0.10, relwidth=0.07, anchor="center")


def run():
    s = open("searches.txt", "r")
    sort = s.readline()
    s.close()
    if sort != 'Name Search':
        load()
        set_values()
    else:
        set_values()


def load():
    #pokemon = "Pokemon.csv"
    name = open("pokemon data.txt", "r")
    var = name.readline()
    name.close()

    s = open("searches.txt", "r")
    sort = s.readline()
    s.close()
    sort = (sort[:-1]).split(",")
    var = (var[:-1]).split(",")
    line_count = 0

    stats_var = sort[4]

    AorD_var = str(sort[5])

    if AorD_var == "False":
        AorD_var = False
    elif AorD_var == "True":
        AorD_var = True


    for i in var:
        line_count = 0

        csvfile = open("Pokemon.csv", 'r')
        pokemon = csv.reader(csvfile)
        for row in pokemon:
            row = list(row)
            if line_count != 0:
                leg = False
                if row[12] == "True":
                    leg = True

                if row[1] == i:
                    r_val[row[1]] = row
            line_count += 1
    return r_val

def type_colour(name, load):
    global r_val
    if load == True:
        TYPE = r_val[name][2]
    else:
        TYPE = name[2]
    if TYPE == 'Normal':
        return '#A8A77A'
    elif TYPE == 'Fire':
        return '#EE8130'
    elif TYPE == 'Water':
        return '#6390F0'
    elif TYPE == 'Electric':
        return '#F7D02C'
    elif TYPE == 'Grass':
        return '#7AC74C'
    elif TYPE == 'Ice':
        return '#96D9D6'
    elif TYPE == 'Fighting':
        return '#C22E28'
    elif TYPE == 'Poison':
        return '#A33EA1'
    elif TYPE == 'Ground':
        return '#E2BF65'
    elif TYPE == 'Flying':
        return '#A98FF3'
    elif TYPE == 'Psychic':
        return '#F95587'
    elif TYPE == 'Bug':
        return '#A6B91A'
    elif TYPE == 'Rock':
        return '#B6A136'
    elif TYPE == 'Ghost':
        return '#735797'
    elif TYPE == 'Dragon':
        return '#6F35FC'
    elif TYPE == 'Dark ':
        return '#705746'
    elif TYPE == 'Steel':
        return '#B7B7CE'
    elif TYPE == 'Fairy':
        return '#D685AD'
    else:
        return '#5778BB'

def set_values():
    global count, r_val, pokemonPicFile, type1File, type2File, typecolour
    # | Id [0] | name [1] | type1 [2] | type2 [3] | Total [4] | hp [5] | Attack [6]
    # | Defense [7] | Sp. Atk [8] | Sp. Def [9] | Speed [10] | Generation [11] | Legendary [12]
    s = open("searches.txt", "r")

    if s.readline() == 'Name Search':
        data = open("pokemon data.txt", "r")
        r_val = data.readline()
        data.close()
        r_val = yaml.load(r_val)

    s.close()

    back_button.place(relx=0.0, rely=0.5,
                      relheight=0.9, relwidth=0.3, anchor="w")
    next_button.place(relx=0.7, rely=0.5,
                      relheight=0.9, relwidth=0.3, anchor="w")

    if count == len(r_val) - 1:
        next_button.place_forget()

    if count == 0:
        back_button.place_forget()

    name = list(r_val)
    name = name[count]

    idName["text"] = f"ID: {r_val[name][0]}"
    pokeName["text"] = f"{r_val[name][1]}"
    # type1Name["text"] = f"{r_val[name][2]}"
    # type2Name["text"] = f"{r_val[name][3]}"
    totalName["text"] = f"Total: {r_val[name][4]}"
    HPName["text"] = f"HP: {r_val[name][5]}"
    attackName["text"] = f"Atk: {r_val[name][6]}"
    defenceName["text"] = f"Def: {r_val[name][7]}"
    spAttackName["text"] = f"Sp.Atk: {r_val[name][8]}"
    spDefenceName["text"] = f"Sp.Def: {r_val[name][9]}"
    speedName["text"] = f"Speed: {r_val[name][10]}"
    generationName["text"] = f"Gen: {r_val[name][11]}"
    legendary = r_val[name][12]

    typecolour = type_colour(name, True)

    frame.place(relx=0.5, rely=0.10,
                width=385, height=472,
                anchor="n")

    frame.config(bg=typecolour)
    if legendary == 'False':  # Creates boolean to avoid errors
        legendary = False
    elif legendary == 'True':
        legendary = True

    #  sets picture
    legendFrame.forget()  # changes the background depending on legendary or not

    if legendary == False:
        legbg = "#9C9FA5"
        legendFrame.config(bg=legbg, highlightbackground="black", highlightthickness=0)

    elif legendary == True:
        legbg = "#D4AF37"
        legendFrame.config(bg=legbg, highlightbackground="black", highlightthickness=0)

    legendFrame.place(relx=0.5, rely=0.18,
                      relheight=0.37, relwidth=0.88,  # replaces after config
                      anchor="n")

    try:
        bg.GenBackground(f"Pokemon Pictures/{r_val[name][1].lower()}.png", "formating/pokeBackShadow.png")
        ss = PhotoImage(file='bg.png')
        #backLabelImage = Label(legendFrame, image=ss)
        #backLabelImage.place(relx=0.5, rely=0.5,
        #                 relheight=0.9, relwidth=0.92, anchor="center")
        #backLabelImage.pack()
        pokemonPicFile.config(file=f'bg.png')
        pokemonPicFile = pokemonPicFile.zoom(7)  # Resizes images
        pokemonPicFile = pokemonPicFile.subsample(3)

        pokemonPic = Label(legendFrame,
                           image=pokemonPicFile, bg="#5778BB")

        pokemonPic.place(relx=0.5, rely=0.5,
                         relheight=0.9, relwidth=0.92, anchor="center")


    except Exception as e:
        # pokemonPicFile = pokemonPicFile.zoom(2)  # Resizes images
        # pokemonPicFile = pokemonPicFile.subsample(1)
        print(e)
        pokemonPicFile.config(file='Pokemon Pictures/missing-image.png')
        pokemonPicFile = pokemonPicFile.zoom(2)  # Resizes images
        pokemonPicFile = pokemonPicFile.subsample(3)

        pokemonPic = Label(legendFrame,
                           image=pokemonPicFile, bg="#5778BB")

        pokemonPic.place(relx=0.5, rely=0.5,
                         relheight=0.9, relwidth=0.92, anchor="center")
    type1File.config(file=f'pokemonTypes/Icon_{r_val[name][2]}.png')
    type1File = type1File.zoom(1)
    type1File = type1File.subsample(3)

    type1Pic = Label(legendFrame,
                     image=type1File, bg="#5778BB")  # bg="#5778BB"

    type1Pic.place(relx=0.915, rely=0.11,
                   relheight=0.10, relwidth=0.07, anchor="center")

    type2File.config(file=f'pokemonTypes/Icon_{r_val[name][3]}.png')
    type2File = type2File.zoom(1)
    type2File = type2File.subsample(3)

    type2Pic = Label(legendFrame,
                     image=type2File, bg="#5778BB")  # bg="#5778BB"

    type2Pic.place(relx=0.83, rely=0.11,
                   relheight=0.10, relwidth=0.07, anchor="center")



def name_set_values():
    global r_val, pokemonPicFile, type1File, type2File, ss, typecolour

    back_button.place(relx=0.0, rely=0.5,
                      relheight=0.9, relwidth=0.3, anchor="w")
    next_button.place(relx=0.7, rely=0.5,
                      relheight=0.9, relwidth=0.3, anchor="w")

    if count == len(r_val) - 1:
        next_button.place_forget()

    if count == 0:
        back_button.place_forget()


    data = open("pokemon data.txt", "r")
    name = data.readline()
    name = list(name)
    print(name)
    idName["text"] = f"ID: {name[0]}"
    pokeName["text"] = f"{name[1]}"
    totalName["text"] = f"Total: {name[4]}"
    HPName["text"] = f"HP: {name[5]}"
    attackName["text"] = f"Atk: {name[6]}"
    defenceName["text"] = f"Def: {name[7]}"
    spAttackName["text"] = f"Sp.Atk: {name[8]}"
    spDefenceName["text"] = f"Sp.Def: {name[9]}"
    speedName["text"] = f"Speed: {name[10]}"
    generationName["text"] = f"Gen: {name[11]}"
    legendary = name[12]

    typecolour = type_colour(name, False)

    frame.place(relx=0.5, rely=0.10,
                width=385, height=472,
                anchor="n")

    frame.config(bg=typecolour)
    if legendary == 'False':  # Creates boolean to avoid errors
        legendary = False
    elif legendary == 'True':
        legendary = True

    #  sets picture
    legendFrame.forget()  # changes the background depending on legendary or not

    if legendary == False:
        legbg = "#9C9FA5"
        legendFrame.config(bg=legbg, highlightbackground="black", highlightthickness=0)

    elif legendary == True:
        legbg = "#D4AF37"
        legendFrame.config(bg=legbg, highlightbackground="black", highlightthickness=0)

    legendFrame.place(relx=0.5, rely=0.18,
                      relheight=0.37, relwidth=0.88,  # replaces after config
                      anchor="n")

    try:

        pokemonPicFile.config(file=f'Pokemon Pictures/{name[1].lower()}.png')
        pokemonPicFile = pokemonPicFile.zoom(7)  # Resizes images
        pokemonPicFile = pokemonPicFile.subsample(3)

        pokemonPic = Label(legendFrame,
                           image=pokemonPicFile, bg="#5778BB")

        pokemonPic.place(relx=0.5, rely=0.5,
                         relheight=0.9, relwidth=0.92, anchor="center")


    except:
        # pokemonPicFile = pokemonPicFile.zoom(2)  # Resizes images
        # pokemonPicFile = pokemonPicFile.subsample(1)
        pokemonPicFile.config(file='Pokemon Pictures/ditto.png')
        pokemonPicFile = pokemonPicFile.zoom(7)  # Resizes images
        pokemonPicFile = pokemonPicFile.subsample(3)

        pokemonPic = Label(legendFrame,
                           image=pokemonPicFile, bg="#5778BB")

        pokemonPic.place(relx=0.5, rely=0.5,
                         relheight=0.9, relwidth=0.92, anchor="center")

    type1File.config(file=f'pokemonTypes/Icon_{name[2]}.png')
    type1File = type1File.zoom(1)
    type1File = type1File.subsample(3)

    type1Pic = Label(legendFrame,
                     image=type1File, bg="#5778BB")  # bg="#5778BB"

    type1Pic.place(relx=0.915, rely=0.11,
                   relheight=0.10, relwidth=0.07, anchor="center")

    type2File.config(file=f'pokemonTypes/Icon_{name[3]}.png')
    type2File = type2File.zoom(1)
    type2File = type2File.subsample(3)

    type2Pic = Label(legendFrame,
                     image=type2File, bg="#5778BB")  # bg="#5778BB"

    type2Pic.place(relx=0.83, rely=0.11,
                   relheight=0.10, relwidth=0.07, anchor="center")

def home_button_push():
    pygame.mixer.music.stop()
    root.destroy()
    os.system('python menu.py')


def next_button_push():
    global count
    count += 1

    set_values()


def back_button_push():
    global count
    count -= 1

    set_values()


# HEX Colours: #9C9FA5 - Grey | #5778BB - Blue | #DFE2EA - white
Music().musicPlay()
Music().musicControls(root)

run()
root.mainloop()

# root.wm_attributes("-transparentcolor", 'grey')