try:
    from tkinter import *
except ImportError:
    from tkinter import *
import csv
"""
put somewhere that python doesn't like other languages (not coding languages)
"""

def info_page_info(list):
    print(f"""\nname: {list[0]} 
gen: {list[2]} 
multiplier: {list[3]}
Additional effect: {list[4]}
description:
{list[5]}""")


list = []
with open("pokeball info.csv","r") as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        if 'ball_name' not in row:
            list.append(row)
            print(row)
while True:
    choice = input("\n[poke/great/ultra/master/safari/fast/level/lure/heavy/love/friend/moon/sport/net/nest/repeat/timer/luxury/premier/dive/dusk/heal/quick/cherish/park/dream/beast]>> ")
    if choice != 'stop':
        if choice == 'poke':
            num = 0
        elif choice == 'great':
            num = 1
        elif choice == 'ultra':
            num = 2
        elif choice == 'master':
            num = 3
        elif choice == 'safari':
            num = 4
        elif choice == 'fast':
            num = 5
        elif choice == 'level':
            num = 6
        elif choice == 'lure':
            num = 7
        elif choice == 'heavy':
            num = 8
        elif choice == 'love':
            num = 9
        elif choice == 'friend':
            num = 10
        elif choice == 'moon':
            num = 11
        elif choice == 'sport':
            num = 12
        elif choice == 'net':
            num = 13
        elif choice == 'nest':
            num = 14
        elif choice == 'repeat':
            num = 15
        elif choice == 'timer':
            num = 16
        elif choice == 'luxury':
            num = 17
        elif choice == 'premier':
            num = 18
        elif choice == 'dive':
            num = 19
        elif choice == 'dusk':
            num = 20
        elif choice == 'heal':
            num = 21
        elif choice == 'quick':
            num = 22
        elif choice == 'cherish':
            num = 23
        elif choice == 'park':
            num = 24
        elif choice == 'dream':
            num = 25
        elif choice == 'beast':
            num = 26
        info_page_info(list[num])
    else:
        break


