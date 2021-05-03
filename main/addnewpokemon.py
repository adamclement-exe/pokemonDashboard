"""
:author Basker12
"""
try:
    from tkinter import *
except ImportError:
    from tkinter import *
import os

root = Tk()
root.title('Add a new Pokemon')

iconFile = PhotoImage(file='formating/ball.png')
root.iconphoto(False, iconFile) # Icon Image

HEIGHT = 642
WIDTH = 405
root.geometry(f'{HEIGHT}x{WIDTH}')

root.minsize(WIDTH, HEIGHT)
root.maxsize(WIDTH, HEIGHT)

background = PhotoImage(file='formating/settingsbackgroundimage.png')

Canvas = Canvas(root, width=WIDTH, height=HEIGHT, highlightbackground='#9C9FA5', highlightthickness='4')
Canvas.pack(fill='both', expand='True')
Canvas.create_image(0, 0, image=background,
                    anchor='nw')

newPokeName = Entry(root, font=('times', 12, 'bold'), borderwidth='4',
                    bg='#9C9FA5',
                    fg='#5778BB')

newPokeName.place(relx=0.25, rely=0.105,
                  relheight=0.09, relwidth=0.5)

newPokeName.insert(0, f'Your new Pokemons name')

newType1 = Entry(root, font=('times', 12, 'bold'), borderwidth='4',
                 bg='#9C9FA5',
                 fg='#5778BB')

newType1.place(relx=0.25, rely=0.210,
               relheight=0.09, relwidth=0.5)

newType1.insert(0, f'Your Pokemons first type')

newType2 = Entry(root, font=('times', 12, 'bold'), borderwidth='4',
                 bg='#9C9FA5',
                 fg='#5778BB')

newType2.place(relx=0.25, rely=0.315,
               relheight=0.09, relwidth=0.5)

newType2.insert(0, f'Your Pokemons second type')

createButton = Button(root, text='CREATE POKEMON', font=('times', 12, 'bold'), borderwidth='4',
                     bg='#9C9FA5',
                     fg='#5778BB',
                     width='15',
                      command=lambda: createdPokemon())

createButton.place(relx=0.25, rely=0.420,
                   relheight=0.09, relwidth=0.5)

def clearText(e): # This definition clears the entry box text, instead having to do it manually

    if newPokeName.get() == 'Your new Pokemons name' or newType1.get() == 'Your Pokemons first type' or newType2.get() == 'Your Pokemons second type':
        newPokeName.delete(0, END)
        newType1.delete(0, END)
        newType2.delete(0, END)

def createdPokemon():

    pokename = newPokeName.get()
    if pokename == pokename:
        name = pokename.title()

    poketype1 = newType1.get()
    if poketype1 == poketype1:
        type1 = poketype1.title()

    poketype2 = newType2.get()
    if poketype2 == poketype2:
        type2 = poketype2.title()

    print(f"This is your new pokemon, his name is {name}, it's first type is {type1}, and it's second type is {type2}")

newPokeName.bind("<Button-1>", clearText) # clearText runs the definition
newType1.bind("<Button-1>", clearText)
newType2.bind("<Button-1>", clearText)

# HEX Colours: #9C9FA5 - Grey | #5778BB - Blue | #DFE2EA - white
root.mainloop()