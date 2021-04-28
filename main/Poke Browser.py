try: from Tkinter import *
except ImportError: from tkinter import *

class Run:
    root = Tk()
    HEIGHT = 500
    WIDTH = 600

    canvas = Canvas(root, height=HEIGHT, width=WIDTH)
    canvas.pack()



    root.mainloop()