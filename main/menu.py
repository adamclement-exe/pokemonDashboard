"""
:author Basker12
:author FSNCryo
"""
try: from Tkinter import *
except ImportError: from tkinter import *

root = Tk()
root.title('Pokemon Index Finder')
root.geometry('500x475')

iconFile = PhotoImage(file='formating/ball.png') #Icon image
root.iconphoto(False, iconFile)

backgroundImage = PhotoImage(file='formating/background.png')
canvas = Canvas(root, width=600, height=500, highlightbackground='#9C9FA5', highlightthickness='4')
canvas.pack(fill='both', expand=True)
canvas.create_image(0, 0, image=backgroundImage, anchor='nw') #Created an image so that text and buttons are able to show the background

canvas.create_text(105, 30, text='DEVS:', font=('times', 50, 'bold'), fill='#9C9FA5', underline='5')
canvas.create_text(98, 180, text='Madmegsox1\n' + 'FSNCryo\n' + 'Basker 12\n' + 'Hiddenmaask\n' + 'PointlessQuack\n' + 'DraconicDroid\n' + 'Squidnugi\n',
                   font=('times', 20, 'bold'), fill='Black')

startButton = Button(root, text='START', font=('times', 15, 'bold'), borderwidth='4',
                     fg='#5778BB',
                     bg='#9C9FA5',
                     width='35',
                     command=lambda: on_button_push())
startButtonWindow = canvas.create_window(250, 400, anchor='center', window=startButton)

def on_button_push():
    print("Test")

#HEX Colours: #9C9FA5 - Grey | #5778BB - Blue | #DFE2EA - white

root.mainloop()
