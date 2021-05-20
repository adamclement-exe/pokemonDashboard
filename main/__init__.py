"""
:author Madmegsox1
:author FSNCryo
:author Basker 12
:author Jaime
"""

import util
import os
import csv
from util import backgroundGenerator as bg

# This is the base of the project

class run:

    def __init__(self):
        Devs = ("Madmegsox1, FSNCryo, HiddenMask, Basker12, PointlessQuack, DraconicDroid, Squidnugi")
        bg.GenBackground("Pokemon Pictures/abra.png", "formating/pokeBackShadow.png")


    def name_search(self):
        s = open("pokemon data.txt", "r")
        pokename_var = s.readline().replace(',', '')
        s.close()
        pokename_var = util.csv_loader("Pokemon.csv").get_pokemon_by_char(pokename_var)

        searches = open("searches.txt", "w")
        line_count = 0

        csvfile = open("Pokemon.csv", 'r')
        pokemon = csv.reader(csvfile)
        #  Grass, Poison, 1, False, Attack, True,

        searches.write(f"Name Search")
        stats = open("pokemon data.txt", "w")
        r_val = {}
        count = 0
        if pokename_var != 0:
            for i in pokename_var:
                i = list(i.values())
                r_val[i[1]] = i

                count += 1

            stats.write(str(r_val))
            stats.close()
            searches.close()

            return len(r_val)
        else:
            return 0



    def refract_search(self):
        s = open("searches.txt", "r")
        var = s.readline()
        s.close()
        var = (var[:-1]).split(",")

        type1_var = str(var[0])
        type2_var = str(var[1])
        stats_var = var[4]

        gen_var = str(var[2])
        if gen_var != 'All':
            gen_var = int(var[2])

        Legendary_var = str(var[3])
        if Legendary_var == "False":
            Legendary_var = False
        elif Legendary_var == "True":
            Legendary_var = True

        AorD_var = str(var[5])
        if AorD_var == "False":
            AorD_var = True
        elif AorD_var == "True":
            AorD_var = False

        a = util.search()
        a = a.getList(stats_var, AorD_var, [type1_var, type2_var, gen_var, Legendary_var])  # filtered search
        names = open("pokemon data.txt", "w")

        if a != 0:
            for i in a:
                names.write(i)
                names.write(",")
            names.close()
            return len(a)
        else:
            return 0

run()