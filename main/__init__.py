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

        type1_var = s.readline()
        type2_var = s.readline()
        gen_var = s.readline()
        Legendary_var = s.readline()
        stats_var = s.readline()
        AorD_var = s.readline()

        a = util.search()
        #print(stats_var+AorD_var+type1_var+type2_var+gen_var+Legendary_var)
        a = a.getList(stats_var, AorD_var, [type1_var, type2_var, gen_var, Legendary_var])
        print(a)
