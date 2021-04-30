"""
dev: Theo
date: 28/04/21
"""

try:
    from Tkinter import *
except ImportError:
    from tkinter import *
import tkinter as tk

# Importing Image class from PIL module
from PIL import ImageTk,Image

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

pokeName["text"] = "[POKE_NAME]"

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

                      command=lambda: on_button_push())  # on_button_push() Runs When a BUTTON is Pushed

back_button.place(relx=0.0, rely=0,
                   height=75, width=100)

homeButtonFile = PhotoImage(file="formating/Home.PNG")  # home Button image

home_button = Button(bottomBar,
                      bg="#DFE2EA",
                      fg="#DFE2EA",
                      image=homeButtonFile,
                      font=("times", 11, "bold"), borderwidth=0,

                      command=lambda: on_button_push())  # on_button_push() Runs When a BUTTON is Pushed

home_button.place(relx=0.37, rely=0.2,
                   height=40, width=100)

nextButtonFile = PhotoImage(file="formating/Next.PNG")  # next Button image

next_button = Button(bottomBar,
                      bg="#DFE2EA",
                      fg="#DFE2EA",
                      image=nextButtonFile,
                      font=("times", 11, "bold"), borderwidth=0,

                      command=lambda: on_button_push())  # on_button_push() Runs When a BUTTON is Pushed

next_button.place(relx=0.75, rely=0,
                   height=75, width=100)


def on_button_push():  # Run Main GUI
    print("Test")


# HEX Colours: #9C9FA5 - Grey | #5778BB - Blue | #DFE2EA - white

root.mainloop()
