try:
    from tkinter import *
except ImportError:
    from tkinter import *
from menu import *

HEIGHT = 500
WIDTH = 500

root = Tk()

root.geometry(f'{HEIGHT}x{WIDTH}')
'''
def linustechtips():
    fontName = entry1.get()
    label1.config(font=f'{fontName}')

button1 = Button(root, text='Click Me!', font=('helvetica', 15),
                 command=lambda: linustechtips())
button1.pack()

label1 = Label(root, text='THIS IS A TEST', font=(f'times', 20))
label1.pack()

entry1 = Entry(root, font=(f'times', 12),
               bg='#9C9FA5',
               fg='#5788BB')

entry1.pack()

entry1.insert(0, 'Write a font')
'''

class Fonts:

    def __init__(self):
        self.OPTIONS = [
            'Times',
            'Comic sans MS',
            'Helvetica',
            'Garamond'
        ]  # list with fonts

        variable = StringVar(root)
        variable.set(self.OPTIONS[0])


        def callback(selection):
            font_drop.config(font=(selection, 12, 'bold'))
            startButton.config(font=(selection, 12, 'bold'))

        font_drop = OptionMenu(root, variable, *self.OPTIONS, command=callback)  # drop down menu for fonts
        font_drop.config(bg='#9C9FA5', fg='#5778BB', font=('times', 12, 'bold'))
        font_drop.place(relx=0.33, rely=0.750,
                relheight=0.075, relwidth=0.35)

font = Fonts()

root.mainloop()