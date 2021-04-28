try:
    from Tkinter import *
except ImportError:
    from tkinter import *
root = Tk()
HEIGHT = 500
WIDTH = 600

root.minsize(WIDTH,HEIGHT)
root.maxsize(WIDTH,HEIGHT)

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

text1["text"] = 'DEVS:'

text2 = Label(root,
              bg='#2E4053',
              fg='white',
              font=('times', 11, 'bold'))

text2.place(relx=0.06, rely=0.3,
            relwidth=0.18, relheight=0.3)

text2[
    "text"] = 'Madmegsox1\n' + 'FSNCryo\n' + 'Basker 12\n' + 'Hiddenmaask\n' + 'PointlessQuack\n' + 'DraconicDroid\n' + 'Squidnugi\n'

start_button = Button(frame1,
                      bg='white',
                      font=('times', 11, 'bold'), borderwidth=4,

                      command=lambda: on_button_push())  # on_button_push() Runs When a BUTTON is Pushed

start_button.place(relx=0.25, rely=0.765,
                   relheight=0.08, relwidth=0.50)

start_button["text"] = f'START'


def on_button_push():  # Run Main GUI
    return


root.mainloop()