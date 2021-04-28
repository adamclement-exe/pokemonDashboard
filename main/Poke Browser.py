try:
    from Tkinter import *
except ImportError:
    from tkinter import *


# Code that runs after menu start button is pressed

print('running')

root = Tk()
HEIGHT = 500
WIDTH = 600

canvas = Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

frame1 = Frame(root,
               bg='#2E4053')

frame1.place(relx=0.5, rely=0.14,
             relwidth=0.90, relheight=0.75,
             anchor='n')

text1 = Label(root,
              bg='#2E4053',
              fg='white',
              font=('times', 11, 'bold'))

text1.place(relx=0.06, rely=0.21,
            relwidth=0.15, relheight=0.09)

text1["text"] = 'POKEMON'
root.mainloop()
