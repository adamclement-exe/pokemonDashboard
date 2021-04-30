"""
:author Madmegsox1
:author FSNCryo
:author Basker 12
:author Jaime
"""

import util


# This is the base of the project

class run():
    def __init__(self):
        print("Project by: Madmegsox1, FSNCryo, HiddenMask, Basker12, PointlessQuack, DraconicDroid, Squidnugi")
        instance = util.csv_loader("Pokemon.csv")
        d = instance.sort("id", True)
        i = instance.refactor_list(d, "type1", "Grass")
        print(i)
        a = instance.refactor_list(i, "gen", 1)
        print(a)



run()
