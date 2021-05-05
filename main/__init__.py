"""
:author Madmegsox1
:author FSNCryo
:author Basker 12
:author Jaime
"""

import util


# This is the base of the project

class run:

    def __init__(self):
        Devs = ("Madmegsox1, FSNCryo, HiddenMask, Basker12, PointlessQuack, DraconicDroid, Squidnugi")

    def name_search(self):
        s = open("searches.txt", "r")
        pokename_var = s.readline()

        print(pokename_var)

    def refract_search(self):
        s = open("searches.txt", "r")
        var = s.readline()
        var = (var[:-1]).split(",")


        type1_var = str(var[0])
        type2_var = str(var[1])
        stats_var = var[4]

        gen_var = str(var[2])
        if gen_var != 'All':
            gen_var = int(var[2])


        Legendary_var = str(var[3])
        if Legendary_var == "False": Legendary_var = False
        elif Legendary_var == "True": Legendary_var = True

        AorD_var = str(var[5])
        if AorD_var == "False": AorD_var = False
        elif AorD_var == "True": AorD_var = True


        a = util.search()
        a = a.getList(stats_var, AorD_var, [type1_var, type2_var, gen_var, Legendary_var])
        print(a)
