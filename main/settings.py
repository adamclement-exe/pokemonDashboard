try:
    from Tkinter import *
except ImportError:
    from tkinter import *

root = Tk()
root.title('Settings')

HEIGHT = 475
WIDTH = 475
root.geometry(f'{WIDTH}x{HEIGHT}')

root.minsize(WIDTH, HEIGHT)
root.maxsize(WIDTH, HEIGHT)

iconFile = PhotoImage(file='formating/ball.png')
root.iconphoto(False, iconFile)


root.mainloop()