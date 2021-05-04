"""
:author Madmegsox1
:author FSNCryo
:author Basker 12
:author Jaime
"""

import util
import searches


# This is the base of the project

class run:
    def __init__(self):
        """
        self.stats_var = searches.stats_var
        self.AorD_var = searches.AorD_var
        self.type1_var = searches.type1_var
        self.type2_var = searches.type2_var
        self.gen_var = searches.gen_var
        self.Legendary_var = searches.Legendary_var
        self.poke_name = searches.poke_name
        """
        print("Project by: Madmegsox1, FSNCryo, HiddenMask, Basker12, PointlessQuack, DraconicDroid, Squidnugi")

    def name_search(self):
        instance = util.csv_loader("Pokemon.csv")
        d = instance.sort("id", True)
        pokename = instance.refactor_list(d, "name", searches.poke_name)
        print(pokename)

    def refract_search(self):
        instance = util.csv_loader("Pokemon.csv")
        #  following code filters the users search
        d = instance.sort(searches.stats_var, searches.AorD_var)

        t1 = instance.refactor_list(d, "type1", searches.type1_var)

        t2 = instance.refactor_list(t1, "type2", searches.type2_var)

        gen = instance.refactor_list(t2, "gen", searches.gen_var)

        leg = instance.refactor_list(gen, "legendary", searches.Legendary_var)
        searches_list = leg

        print(searches_list)


run()
