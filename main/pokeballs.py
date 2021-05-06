try:
    from tkinter import *
except ImportError:
    from tkinter import *
import csv
"""
put somewhere that python doesn't like other languages (not coding languages)
"""

def info_page_info(list):
    print(f"""name:{list[0]} 
gen:{list[2]} 
multiplier:{list[3]}
Additional effect:{list[4]}
description:
{list[5]}""")


list = []
with open("pokeball info.csv","r") as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        if 'ball_name' not in row:
            list.append(row)
            print(row)

info_page_info(list[0])
