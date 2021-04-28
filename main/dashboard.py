"""
dev: Theo
date: 28/04/21
"""

try:
    from Tkinter import *
except ImportError:
    from tkinter import *
import tkinter as tk

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

text2 = Label(root,
              bg="#2E4053",
              fg="white",
              font=("times", 11, "bold"))

text2.place(relx=0.06, rely=0.3,
            relwidth=0.18, relheight=0.3)

text2["text"] = (
        "Madmegsox1\n" + "FSNCryo\n" + "Basker 12\n" + "Hiddenmaask\n" + "PointlessQuack\n" + "DraconicDroid\n" + "Squidnugi\n")

start_button = Button(frame,
                      bg="#9C9FA5",
                      fg="#DFE2EA",
                      font=("times", 11, "bold"), borderwidth=4,

                      command=lambda: on_button_push())  # on_button_push() Runs When a BUTTON is Pushed

start_button.place(relx=0.25, rely=0.765,
                   relheight=0.08, relwidth=0.50)

start_button["text"] = f"START"


def on_button_push():  # Run Main GUI
    print("Test")


# HEX Colours: #9C9FA5 - Grey | #5778BB - Blue | #DFE2EA - white

root.mainloop()
