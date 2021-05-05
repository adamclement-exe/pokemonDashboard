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
import tkinter as tk

# Importing Image class from PIL module
from PIL import ImageTk, Image

root = Tk()

HEIGHT = 642
WIDTH = 405

root.minsize(WIDTH,HEIGHT)
root.maxsize(WIDTH,HEIGHT)
root.title("Pokemon Index Finder")
iconFile = PhotoImage(file="formating/ball.png")  # Icon image
root.iconphoto(False, iconFile)




canvas = Canvas(root, height=HEIGHT, width=WIDTH, bg="#9C9FA5", highlightbackground="black", highlightthickness=2)
canvas.pack()

type1PicFile = PhotoImage(file="pokemonTypes/Icon_Ice.png")        # change image with the filtered type from csv
canvas.create_image(0, 100, image=type1PicFile)



#needs a if type2 exists function here when implementing

type2PicFile = PhotoImage(file="pokemonTypes/Icon_Ice.png")        # change image with the filtered type from csv
canvas.create_image(0, 100, image=type2PicFile)

frame = Frame(canvas,
              bg="#5778BB", highlightbackground="black", highlightthickness=5)

frame.place(relx=0.5, rely=0.10,
            width=385, height=472,
            anchor="n")


bottomBar = Frame(root,
                  bg="#DFE2EA", highlightbackground="black", highlightthickness=1)      #Adds Background Shape

bottomBar.place(relx=0.5, rely=0.85,
                width=WIDTH-10, height=86,
                anchor="n")

legendFrame = Frame(root,
              bg="#D4AF37", highlightbackground="black", highlightthickness=0)

legendFrame.place(relx=0.5, rely=0.18,
            relheight=0.37, relwidth=0.88,
            anchor="n")

legendary = 1       #Placeholder

if legendary == 0:
    legendFrame.config(bg="#9C9FA5", highlightbackground="black", highlightthickness=0)

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
                 font=("times", 11, "bold"))  # formatting text

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



#type1Pic.place(relx=0.5, rely=0.5,
                 #relheight=0.9, relwidth=0.92, anchor="center")



generationName = Label(root,
                       bg="#2E4053",
                       fg="#DFE2EA",
                       font=("times", 11, "bold"))

generationName.place(relx=0.35, rely=0.56,
                     relwidth=0.3, relheight=0.05)

generationName["text"] = "[GENERATION]"     #Value for placeholder

attackName = Label(root,
                       bg="#2E4053",
                       fg="#DFE2EA",
                       font=("times", 11, "bold"))

attackName.place(relx=0.08, rely=0.63,
                     relwidth=0.2, relheight=0.05)

attackName["text"] = "[ATTACK]"

defenceName = Label(root,
                       bg="#2E4053",
                       fg="#DFE2EA",
                       font=("times", 11, "bold"))

defenceName.place(relx=0.4, rely=0.63,
                     relwidth=0.2, relheight=0.05)

defenceName["text"] = "[DEFENCE]"

spAttackName = Label(root,
                       bg="#2E4053",
                       fg="#DFE2EA",
                       font=("times", 11, "bold"))

spAttackName.place(relx=0.08, rely=0.73,
                     relwidth=0.2, relheight=0.05)

spAttackName["text"] = "[SP.ATTACK]"

spDefenceName = Label(root,
                       bg="#2E4053",
                       fg="#DFE2EA",
                       font=("times", 11, "bold"))

spDefenceName.place(relx=0.4, rely=0.73,
                     relwidth=0.2, relheight=0.05)

spDefenceName["text"] = "[SP.DEFENCE]"

speedName = Label(root,
                       bg="#2E4053",
                       fg="#DFE2EA",
                       font=("times", 11, "bold"))

speedName.place(relx=0.72, rely=0.68,
                     relwidth=0.2, relheight=0.05)

speedName["text"] = "[SPEED]"
#formating/imagePlace.PNG

pokemonPicFile = PhotoImage(file="Pokemon Pictures/abomasnow.png")  # change image with the filtered pokemon

pokemonPicFile = pokemonPicFile.zoom(2)             #Resizes images
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

                     command=lambda: on_button_push())  # on_button_push() Runs When a BUTTON is Pushed

back_button.place(relx=0.0, rely=0.5,
                  relheight=0.9, relwidth=0.3,anchor="w")

homeButtonFile = PhotoImage(file="formating/Home.PNG")  # home Button image

home_button = Button(bottomBar,
                     bg="#DFE2EA",
                     fg="#DFE2EA",
                     image=homeButtonFile,
                     font=("times", 11, "bold"), borderwidth=0,

                     command=lambda: on_button_push())  # on_button_push() Runs When a BUTTON is Pushed

home_button.place(relx=0.35, rely=0.5,
                  relheight=0.9, relwidth=0.3,anchor="w")

nextButtonFile = PhotoImage(file="formating/Next.PNG")  # next Button image

next_button = Button(bottomBar,
                     bg="#DFE2EA",
                     fg="#DFE2EA",
                     image=nextButtonFile,
                     font=("times", 11, "bold"), borderwidth=0,

                     command=lambda: on_button_push())  # on_button_push() Runs When a BUTTON is Pushed

next_button.place(relx=0.7, rely=0.5,
                  relheight=0.9, relwidth=0.3,anchor="w")

def on_button_push():  # Run Main GUI
    print("Test")


# HEX Colours: #9C9FA5 - Grey | #5778BB - Blue | #DFE2EA - white

root.mainloop()
