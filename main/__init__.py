"""
:author Madmegsox1
:author FSNCryo
:author Basker 12
"""

import util
# This is the base of the project

class run():
    def __init__(self):
        print("Project by: Madmegsox1, FSNCryo, HiddenMask, Basker12, PointlessQuack, DraconicDroid, Squidnugi")
        print(util.csv_loader("Pokemon.csv").get_pokemon("Bulbasaur"))

run()
