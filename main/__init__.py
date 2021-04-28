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
        print(instance.sort("id", True))


run()
